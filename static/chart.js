function drawChart() {
    var chart = new google.visualization.PieChart(document.getElementById('piechart'));

    $.ajax({
      url: "/pokemons/types"
    }).done(function(response) {
        var types = response.types;

        types.unshift(['Type', 'Total']);

        chart.draw(google.visualization.arrayToDataTable(types));
    });
}

google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);