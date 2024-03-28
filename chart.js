<script type="text/javascript">
    // Load the Visualization API and the corechart package.
google.charts.load("current", { packages: ["corechart"] });

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawChart() {
  var data = new google.visualization.DataTable();

  // Call heart_data_processing to populate the data table
  heart_data_processing(data, heart_rate_data_list);

  // Set chart options
  var options = {
    title: "How much time was spent in each zone?",
    width: 400,
    height: 300,
  };

  // Instantiate and draw our chart, passing in some options.
  var chart = new google.visualization.PieChart(
    document.getElementById("chart_div")
  );
  chart.draw(data, options);
}


// model of MVC

function heart_data_processing(result_data, heart_rate_data) {
  // Initialize variables to count the time spent in each zone
  var out_of_range = 0;
  var fat_burn = 0;
  var cardio = 0;
  var peak = 0;

  // Iterate through the heart rate zones data and update counts
  heart_rate_data.forEach(function(zone) {
    switch (zone.name) {
      case "Out of Range":
        out_of_range += zone.minutes;
        break;
      case "Fat Burn":
        fat_burn += zone.minutes;
        break;
      case "Cardio":
        cardio += zone.minutes;
        break;
      case "Peak":
        peak += zone.minutes;
        break;
      default:
        break;
    }
  });

  // Create the data table and add rows
  result_data.addColumn("string", "Element");
  result_data.addColumn("number", "Minutes");
  result_data.addRows([
    ["Out of Range", out_of_range],
    ["Fat Burn", fat_burn],
    ["Cardio", cardio],
    ["Peak", peak],
  ]);
}

</script>
