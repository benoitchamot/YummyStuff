function voteClick(button_value) {
    let vote_text = `Vote for ${d3.select("#selRecipe").node().value}: ${button_value}`; 
    console.log(vote_text);
}

function optionChanged(value){
    

    // Look for index of selected recipe in data
    let index = 0;

    for(let i in data.name) {
        if (data.name[i] === value){index = i;}
    }

    d3.select("#recipe_name").text(data.name[index]);
    d3.select("#image").html(`<img src="${data.img[index]}" width=400px/>`);
    d3.select("#recipe_rating").text(`${data.stars[index]} From ${data.votes[index]}.`)
    d3.select("#recipe_link").attr('href',data.link[index])
}

function countProperties(obj) {
    var count = 0;

    for(var prop in obj) {
        if(obj.hasOwnProperty(prop))
            ++count;
    }

    return count;
}

function listOptions(data){
    // Populate the dropdown menu with all the available ids
        let dropDownMenu = d3.select("#selRecipe");

        let length = countProperties(data.name);
        console.log(length);
    
        // Loop through the samples
        for (let i=0; i<length; i++){
            // Add the sample id to the dropdown menu
            dropDownMenu.append("option")
                .attr("value", data.name[i])
                .text(data.name[i]);
        }

        optionChanged(data.name[0])
    }
    

console.log(data)
listOptions(data)