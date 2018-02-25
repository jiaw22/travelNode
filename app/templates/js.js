$(document).ready(function() {
    var max_fields      = 5; //maximum input boxes allowed
    var wrapper         = $(".input_fields_wrap"); //Fields wrapper
    var add_button      = $(".add_field_button"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div><input type="text" id=location'+x+' name="mytext[]" placeholder="Fill in location"/><a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });

    $(wrapper).on("click",".remove_field", function(e){ //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    })
});

{
  "addresses": ["New York, NY", "San Francisco, CA", "Cupertino, CA", "Los Angeles, CA", "San Diego, CA"],
  "leg1": {
    "transport": "Car",
    "legTime": 4,
    "legDist": 10,
    "cost": 0
  },
  "leg2": {
    "transport": "Walking",
    "legTime": 2,
    "legDist": 5,
    "cost": 0
  },
  "leg3": {
    "transport": "Uber",
    "legTime": 4,
    "legDist": 10,
    "cost": 15
  },
  "leg4": {
    "transport": "Car",
    "legTime": 20,
    "legDist": 90,
    "cost": 0
  },
  "totaltime" : 4,
  "totaldistance": 50,
  "totalcost": 10,
  "warning": "false"
}
