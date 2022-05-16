// load pins
function loadPins(){

    for (i = 0 ; i < pins.length; i++){       

        // if correct champ selected, load said champ's pins
        if (abilityFilter){
            if (pins[i][0] == champ && pins[i][1] == ability){

                // new marker -> i|0 -> champ, i|1 -> ability, i|2 -> x, i|3 -> y, i|4 -> pin note/name, i|5 child-pins
                const newMarker = L.marker([pins[i][2], pins[i][3]], 
                {icon: new ValorantIcon({iconUrl: "./img/abilityIcons/" + 
                pins[i][1] +".webp"  })}).addTo(mainPinGroup);
                newMarker.bindPopup("<b> " + pins[i][4] + " </b>");

                // store children pins in constant variable to allow multiple children across multiple pins
                const newMarkerChildren = pins[i][5];

                newMarker.on('click', function (e) {

                    // reset all current child pins so that no other child pins are active
                    childPinGroup.clearLayers();

                    for (i = 0; i < newMarkerChildren.length; i++){
                        
                        // make new child pin
                        const newMarkerChild = L.marker([newMarkerChildren[i][0],newMarkerChildren[i][1]],
                            {icon: new LineupIcon({iconUrl: "./img/abilityIcons/pinImg.png" })}).addTo(childPinGroup);
                        
                        newMarkerChild.bindPopup('<iframe style="border-radius: 3%;" src=' + newMarkerChildren[i][3] +
                        ' width="500" height="315" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>', 
                        {keepInView: false,autoPan: false,closeButton: false,maxWidth: 1000});

                    }
                })
            }
        } else {

            if (pins[i][0] == champ){

                // new marker -> i|0 -> champ, i|1 -> ability, i|2 -> x, i|3 -> y, i|4 -> pin note/name, i|5 child-pins
                const newMarker = L.marker([pins[i][2], pins[i][3]], {icon: new ValorantIcon({iconUrl: "./img/abilityIcons/" +
                pins[i][1] +".webp"  })}).addTo(mainPinGroup);
                newMarker.bindPopup("<b> " + pins[i][4] + " </b>");

                // store children pins in constant variable to allow multiple children across multiple pins
                const newMarkerChildren = pins[i][5];

                newMarker.on('click', function (e) {

                    // reset all current child pins so that no other child pins are active
                    childPinGroup.clearLayers();

                    for (i = 0; i < newMarkerChildren.length; i++){
                        
                        // make new child pin
                        const newMarkerChild = L.marker([newMarkerChildren[i][0],newMarkerChildren[i][1]],
                            {icon: new LineupIcon({iconUrl: "./img/abilityIcons/pinImg.png" })}).addTo(childPinGroup);
                        
                        newMarkerChild.bindPopup('<iframe style="border-radius: 3%;" src=' + newMarkerChildren[i][3] +
                        ' width="500" height="315" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>', 
                        {keepInView: false,autoPan: false,closeButton: false,maxWidth: 1000});

                    }
                })
            }
        }
    }
}