alert("Script successfully linked!")

var doctors = ["Dr. Asteeks", "Dr. Chen", "Dr. Bane", "Dr. Brown", "Dr. Baker", "Dr. Campbell", "Dr. Coxs ", "Dr. Rodriguez ", "Dr. Patel ", "Dr. Abels", "Dr. Gangsta ", "Dr. Liu"];

var Months = ["Janurary", "Feburary", "March", "April", "May" , "June", "July", "August" , "September", "October", "November", "December"];

var date = new Date();

var monthValue = date.getMonth();
var month = Months[monthValue];
var year = date.getFullYear();

document.getElementById('mnthAndYr').innerHTML = month + " " + year;

function getDoctors(){

    var select = document.getElementById('doctors');

    var doctorName = '';

    for(var i = 0; i < 4; i++) {
        var choice = document.createElement('option');
        doctorName = doctors[Math.floor(Math.random() * doctors.length)];
        choice.innerHTML = doctorName;
        choice.value = doctorName.replace("Dr. ", '');
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


            