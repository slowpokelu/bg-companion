let rng = `
<button class='w3-button w3-round-large w3-hover-purple' onclick="flip_coin()">Coinflip</button>
<button class='w3-button w3-round-large w3-hover-purple' onclick="random_number(4)">d4</button>
<button class='w3-button w3-round-large w3-hover-purple' onclick="random_number(6)">d6</button>
<button class='w3-button w3-round-large w3-hover-purple' onclick="random_number(8)">d8</button>
<button class='w3-button w3-round-large w3-hover-purple' onclick="random_number(10)">d10</button>
<button class='w3-button w3-round-large w3-hover-purple' onclick="random_number(12)">d12</button>
<button class='w3-button w3-round-large w3-hover-purple' onclick="random_number(20)">d20</button>
<button class='w3-button w3-round-large w3-hover-purple' onclick="random_number(100)">d100</button>
`;
// <button class='w3-button w3-round-large w3-hover-purple' onclick="random_number_input()">Random Number</button>

let links = `
<a href='https://deckstats.net/' target='_blank'>Deckstats</a><br>
<a href='https://www.moxfield.com/' target='_blank'>Moxfield</a><br>
<a href='https://scryfall.com/' target='_blank'>Scryfall</a><br>
<a href='https://www.cardmarket.com/en/Magic' target='_blank'>CardMarket</a><br>
<a href='https://edhrec.com/' target='_blank'>EDHRec</a><br>
<a href='https://spelltable.com/' target='_blank'>Spelltable</a><br>
<a href='https://cedh-decklist-database.com/' target='_blank'>cEDH Decklist Database</a><br>
<a href='https://mpcfill.com/' target='_blank'>MPC Fill</a><br>
<a href='https://makeplayingcards.com/' target='_blank'>MPC</a><br>
`;

let fileInput = `
<p>Choose Collection / Deck file (.txt)</p>
<input class="" id='selectedfile' type='text' name='selectedfile'>
<input class="w3-btn" id='inputfile' type='file' name='inputfile' onChange='showSelectedFile()'>
<br><br>
<pre id="output"></pre>
`

let hp=40;
let lifetracker = `
<p>Only tracks 1 player for the time being :)</p>
<button class="w3-button w3-round-large w3-hover-purple" id="addhpbutton">+</button>
<span><h1>${hp}</h1></span>
<button class="w3-button w3-round-large w3-hover-purple" id="subhpbutton">-</button>
`

function hide_all(){
    const collection = document.getElementsByClassName("hidden");
    for (let i = 0; i < collection.length; i++) {
        collection[i].style.visibility = "hidden";
      }
}

function toggle_dark_white() {
    var element = document.body;
    element.classList.toggle("white-mode");
}

function updateLifetracker(newhp) {

    let lifetracker = `
        <p>Only tracks 1 player for the time being :)</p>
        <button class="w3-button w3-round-large w3-hover-purple" id="addhpbutton">+</button>
        <span><h1>${newhp}</h1></span>
        <button class="w3-button w3-round-large w3-hover-purple" id="subhpbutton">-</button>
        `
    var element = document.getElementById("menu");
    element.style.visibility = "visible";
    element.innerHTML= lifetracker;
    addTrackerEventListener();
    
}

function showLifetracker(){
    hp=40;
    hide_all();
    var element = document.getElementById("menu");
    element.style.visibility = "visible";
    updateLifetracker(40);
}

function addTrackerEventListener(){
    let addhpbutton = document.getElementById("addhpbutton");
    let subhpbutton = document.getElementById("subhpbutton");

    addhpbutton.addEventListener('click', function() {
        hp++;
        updateLifetracker(hp);
    });

    subhpbutton.addEventListener('click', function() {
        hp--;
        updateLifetracker(hp);
    });
}

function flip_coin(){
    
    const res = Math.round(Math.random());
   
    console.log(res);
}

function random_number(max){
    const res = Math.floor(Math.random() * max+1);

    console.log(res);
}

function show_resources(){
    hide_all();
    const element = document.getElementById("menu");
    element.style.visibility = "visible";
    element.innerHTML = links;
}

function openCollection() {
    hide_all();
    const element = document.getElementById("menu");
    element.style.visibility = "visible";
    element.innerHTML = fileInput;
    document.getElementById('inputfile')
        .addEventListener('change', function() {
        var fr=new FileReader();
        fr.onload=function(){
            document.getElementById('output')
                    .textContent=fr.result;
        }
        fr.readAsText(this.files[0]);
        })
}

function showSelectedFile(){
    selectedfile.value= document.getElementById("inputfile").value; 
}

