var CHART_ID = "chart";
var R = null;

var FRACTION_WIDTH = 5;
var FRACTION_MARGIN = 4;
var DEPUTAT_MARGIN = 2;

var CONVOCATION_MARGIN = 100;

window.onload = function () {
    var chartObject = document.getElementById(CHART_ID);
    var chartWidth = chartObject.clientWidth;
    var chartHeight = chartObject.clientHeight;

    CONVOCATION_MARGIN = (chartWidth - FRACTION_WIDTH) / (Object.keys(convocations).length - 1);

    R = Raphael(CHART_ID);

    for (var fraction_id in fractions)
        drawFraction(fractions[fraction_id]);

    for (var deputy_id in deputies)
        drawDeputyWorks(deputies[deputy_id].works);
}

function getFractionPosition(fraction_id) {
    var fraction = fractions[fraction_id];
    return [(fraction['convocation_id'] - 1) * CONVOCATION_MARGIN, 
        fraction['previous_fractions_count'] * FRACTION_MARGIN + fraction['previous_deputies_count'] * DEPUTAT_MARGIN]
}

function drawFraction(fraction) {
    var position = getFractionPosition(fraction['id']);
    var x = position[0];
    var y = position[1];
    var height = fraction['deputies_count'] * DEPUTAT_MARGIN;

    R.rect(x, y, FRACTION_WIDTH, height).attr({
        fill: "silver",
        "stroke-width": 0
    });
}

function drawPath(a, b, direct) {
    var start = [a[0], a[1]];
    var end = [b[0], b[1]];
    var centre = [(start[0] + end[0]) / 2.0, (start[1] + end[1]) / 2.0];

    var w = end[0] - start[0];
    var h = Math.abs(end[1] - start[1]);

    var d = w / 2.0 * (0.15 + 0.4 * h / Math.sqrt(w * w + h * h));

    var path = R.path("M " + start[0] + "," + start[1] +
        "Q " + (start[0] + d) + "," + start[1] + "," + centre[0] + "," + centre[1] +
        "Q " + (end[0] - d) + "," + end[1] + "," + end[0] + "," + end[1]);

    if (direct)
        path.attr({
            'stroke': 'black'
        });
    else
        path.attr({
            'stroke': 'red'
        });

    return path;
}

function drawDeputyWorks(works) {
    for (var i = 0; i < works.length; i++) {
        var start_fraction_position = getFractionPosition(works[i]['fraction_id']);
        var start_x = start_fraction_position[0];
        var start_y = start_fraction_position[1] + works[i]['previous_deputies_count'] * DEPUTAT_MARGIN;
        R.rect(start_x, start_y, FRACTION_WIDTH, 1).attr({
            fill: "black",
            "stroke-width": 0
        });

        if (i < works.length - 1) {
            var stop_fraction_position = getFractionPosition(works[i + 1]['fraction_id']);
            var stop_x = stop_fraction_position[0];
            var stop_y = stop_fraction_position[1] + works[i + 1]['previous_deputies_count'] * DEPUTAT_MARGIN;

            var direct = fractions[works[i + 1]['fraction_id']]['convocation_id'] -
                fractions[works[i]['fraction_id']]['convocation_id'] == 1;
            drawPath([start_x, start_y], [stop_x, stop_y], direct);
        }
    }
}