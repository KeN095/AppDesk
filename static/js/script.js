alert("Script successfully linked!")

var doctors = ["Dr. Asteeks", "Dr. Chen", "Dr. Bane", "Dr. Brown", "Dr. Baker", "Dr. Campbell", "Dr. Coxs ", "Dr. Rodriguez ", "Dr. Patel ", "Dr. Abels", "Dr. Abraham ", "Dr. Liu"];

var Months = ["Janurary", "Feburary", "March", "April", "May" , "June", "July", "August" , "September", "October", "November", "December"];

var days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

var date = new Date();

var monthValue = date.getMonth();
var month = Months[monthValue];
var year = date.getFullYear();

document.getElementById('mnthAndYr').innerHTML = month + " " + year;

var element = document.getElementById("daysOfWeek");

for (var i = 0; i < days.length; i++){
    var tableHeader = document.createElement("th");
    var day = document.createTextNode(days[i]);
    tableHeader.appendChild(day);
    element.appendChild(tableHeader);
}

//Fix duplicate doctors showing up in a day
function getDoctors(){

    var select = document.getElementById('doctors');

    var doctorName = '';

    for(var i = 0; i < 4; i++) {
        var choice = document.createElement('option');
        doctorName = doctors[Math.floor(Math.random() * doctors.length)];
        choice.innerHTML = doctorName;
        select.appendChild(choice);
    }
}


function incrementHeader(){

    if (monthValue + 1 == Months.length){
        //If you reach December, revert back to janurary and increment the year
        alert("No more!");
    }else{
        //Just increment the month
        monthValue = monthValue + 1;
        document.getElementById('mnthAndYr').innerHTML = Months[monthValue] + " " + year;
    }
}

function decrementHeader(){

    if(monthValue == date.getMonth()){

        alert("No less!");
        //Grey out the left arrow because you do not want to user to go back to any other month before the current month
    } else{
        monthValue = monthValue - 1;
        document.getElementById('mnthAndYr').innerHTML = Months[monthValue] + " " + year;
    }
}

function unhideForm(){
    document.getElementById('aptdetails').style.display = "block";
    var element = document.getElementById('aptdetails');

    element.scrollIntoView();

    getDoctors();           
}            