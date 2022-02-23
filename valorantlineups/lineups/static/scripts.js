// map varibles 
var map;
var champ;
var ability;
var calloutState = false;
var abilityFilter = false;

var champs = ['Breach', 'Brimstone', 'Cypher', 'Jett', 'Omen', 'Phoenix', 'Raze', 'Reyna', 'Sage', 'Sova', 'Viper'];
var abilities = [
                    ['Aftershock', 'Flashpoint', 'Fault_Line', 'Rolling_Thunder'],
                    ['Incendiary', 'Stim_Beacon', 'Sky_Smoke', 'Orbital_Strike'], 
                    ['Trapwire', 'Cyber_Cage', 'Spycam', 'Neural_Theft'],
                    ['Cloudburst', 'Updraft', 'Tailwind', 'Blade_Storm'],
                    ['Shrouded_Step', 'Paranoia', 'Dark_Cover', 'From_Shadow'],
                    ['Blaze', 'Curveball', 'Hot_Hands', 'Run_it_Back'],
                    ['Boom_Bot', 'Blast_Pack', 'Paint_Shells', 'Showstopper'],
                    ['Leer', 'Devour', 'Dismiss', 'Empress'],
                    ['Barrier_Orb', 'Slow_Orb', 'Healing_Orb', 'Resurrection'],
                    ['Shock_Bolt', 'Owl_Drone', 'Recon_Bolt', "Hunter's Fury"],
                    ['Snake_Bite', 'Poison_Cloud', 'Toxic_Screen', "Viper's_Pit"]
                ];

// ability icon class 
var ValorantIcon = L.Icon.extend({
    options: {
        iconSize:     [24, 24],
        shadowSize:   [0, 0],
        iconAnchor:   [12, 12],
        shadowAnchor: [0, 0],
        popupAnchor:  [0, -12]
    }
});

// child icon class 
var LineupIcon = L.Icon.extend({
    options: {
        iconSize:     [8, 8],
        shadowSize:   [0, 0],
        iconAnchor:   [4, 4],
        shadowAnchor: [0, 0],
        popupAnchor:  [0, -4]
    }
});

// change champ function called on button press -> string formatting
function changeChamp(champSelection){

    /*
    abilityFilter = false;

    // change current champ variable
    champ = champSelection;

    // champ audio array to choose random champ sfx on select
    var champAudio = ["static/sfx/champLines/" + champ.toLowerCase() + "/" + champ.toLowerCase() + "1.wav", "static/sfx/champLines/" + champ.toLowerCase() + "/" + champ.toLowerCase() + "2.wav", "static/sfx/champLines/" + champ.toLowerCase() + "/" + champ.toLowerCase() + "3.wav"]

    // create quick function to grab champ choice and format
    champGet = (element) => element == champ

    // ability variables taken from champ array
    ability1 = '"' + abilities[champs.findIndex(champGet)][0] + '"';
    ability2 = '"' + abilities[champs.findIndex(champGet)][1] + '"';
    ability3 = '"' + abilities[champs.findIndex(champGet)][2] + '"';
    ability4 = '"' + abilities[champs.findIndex(champGet)][3] + '"';

    // change champ 
    document.getElementById('agentImg').src = "static/img/champIcons/" + champ + "_icon.webp";
    document.getElementById('agentText').innerText = champ;

    // setup ability dropdown 
    document.getElementById('ability1').innerHTML = "<button href='#' onclick='changeAbility("+ ability1 +")'>" + ability1.replace(/"/g, " ").replace(/_/g, " ") + "</button>"
    document.getElementById('ability2').innerHTML = "<button href='#' onclick='changeAbility("+ ability2 +")'>" + ability2.replace(/"/g, " ").replace(/_/g, " ") + "</button>"
    document.getElementById('ability3').innerHTML = "<button href='#' onclick='changeAbility("+ ability3 +")'>" + ability3.replace(/"/g, " ").replace(/_/g, " ") + "</button>"
    document.getElementById('ability4').innerHTML = "<button href='#' onclick='changeAbility("+ ability4 +")'>" + ability4.replace(/"/g, " ").replace(/_/g, ' ') + "</button>"

    // get audio
    var audio = document.getElementById('audioPlayer')

    audio.src = champAudio[Math.floor(Math.random() * champAudio.length)];

    audio.play()

    // reset pins each load (change champ)
    mainPinGroup.clearLayers();
    childPinGroup.clearLayers();
    loadPins();*/
    

    mainPinGroup.clearLayers();
    childPinGroup.clearLayers();
    mapPins(viewedMap, champSelection)
    console.log(viewedMap + " " + champSelection)

}

// change ability function (called when abilities are filtered)
function changeAbility(selectedAbility){

    abilityFilter = true;

    mainPinGroup.clearLayers();

    ability = selectedAbility;

    childPinGroup.clearLayers();

}



// callout enabler to flip each time button pressed
function calloutEnabler(){
    
    calloutsImage = document.getElementById('mapImg2');

    if (calloutState == true){
        calloutState = false;
        calloutsImage.className = 'fade-out';
    }
    else {
        calloutState = true;
        calloutsImage.className = 'fade-in';
    }
}

var jData = "waiting";

function makePin(x, y, i, cIds){

    const newMarker = L.marker([x, y], 
        {icon: new ValorantIcon({iconUrl: "static/img/abilityIcons/" + 
        jData[i].fields.ability +".webp"  })}).addTo(mainPinGroup);

    newMarker.on('click', function (e) {

        // reset all current child pins so that no other child pins are active
        childPinGroup.clearLayers();

        for  (pin of cIds){

            const newMarkerChild = L.marker([cLineups[pin-1].fields.xPos, cLineups[pin-1].fields.yPos], 
            {icon: new LineupIcon({iconUrl: "static/img/abilityIcons/pinImg.png" })}).addTo(childPinGroup);

            newMarkerChild.bindPopup('<iframe style="border-radius: 3%;" src=' + cLineups[pin-1].fields.content + 
            ' width="500" height="315" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>', 
            {keepInView: false,autoPan: false,closeButton: false,maxWidth: 1000});
        }
    })
}

function mapPins(curMap, curAgent){
    for (let i = 0, len = jData.length; i < len; i++){

        if (jData[i].fields.map == curMap && jData[i].fields.character == curAgent){

            var childLineupIds = [];

            for (let j = 0; j < jData[i].fields.childPinIds.ids.length; j++){

                childLineupIds.push(jData[i].fields.childPinIds.ids[j].id)

                

            }

            
            makePin(jData[i].fields.xPos, jData[i].fields.yPos, i, childLineupIds);
            

        }

    }

    console.log(childLineupIds)

}

function hereData(data){
    jData = JSON.parse(data['Lineups'])
    console.log(JSON.parse(data['Lineups']))
    //jData = data;

}

async function retrievePins(){

    await $.ajax({
        url: '/lineups_list',
        datatype: 'json',
        type: 'GET',
        success: hereData,
    });

    await $.ajax({
        url: '/child_lineups_list',
        datatype: 'json',
        type: 'GET',
        success: function (response){

            cLineups = JSON.parse(response['Child Lineups'])
            console.log(JSON.parse(response['Child Lineups']))

        },
    });

    //mapPins("HA", "SA")


}

// init leaflet map
var map = L.map('map', {
    crs: L.CRS.Simple,
    minZoom: -2,
    maxZoom: 1
});

// init main + child pin groups allowing to clear them
var mainPinGroup = L.layerGroup().addTo(map);
var childPinGroup = L.layerGroup().addTo(map);

var bounds = [[0,0], [4096,4096]];

map.fitBounds(bounds);

retrievePins();

//alert(jData[0].fields.xPos);
//makePin(jData[0].fields.xPos, jData[0].fields.yPos);
