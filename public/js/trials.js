let ratios = [2, 3, 4, 5];
let types = ['areas', 'lines']
let countString = localStorage.getItem('trialCount')
let currentCount = JSON.parse(countString)

// set path for the next page
let current_type = location.href.split("/").slice(-1)[0].split('.')[0]
let button = document.getElementById("trial-next")

// select a random ratio
const typeCount = currentCount[current_type]
let curRatio = getRandomAndRemove(typeCount)
currentCount[current_type] = typeCount


// button.setAttribute("onclick", "location.href='" + types[Math.floor(Math.random() * 2)] + ".html';")


// udpate count
updateCount(current_type)

// renders the current page on loaded
renderTrial(current_type);

// renders the next page
renderPages()

// maybe switch the postion of the pairs
maybeSwitchElements(document.getElementById('left-svg'), document.getElementById('right-svg'))


// function that renders different types of trials
function renderTrial(type) {
    switch (type) {
        case 'lines':
            //renders the line according to the ratio
            let right_line = document.getElementById("right-line")
            new_length = 300 - ratios[curRatio] * 60
            right_line.setAttribute("y2", new_length.toString())

            // change the speech text of the new area
            let text = document.getElementById("line-text")
            let new_text = "A line with a length of " + (300 - new_length).toString() + " pixels."
            text.innerHTML = new_text
            
            break;
        
        case 'areas':
            let base_area = 65

            // renders the new area according to the ratio
            let right_area = document.getElementById("right-area")
            new_radius = Math.pow(ratios[curRatio], 1 / 2) * base_area
            right_area.setAttribute("r", new_radius.toString().substring(0, 8))

            break;

        case 'angles':
            let base_angle = 18


    }
}

function renderPages() {
    let avTypes = []
    let i = 0
    while (i < types.length) {
        if (currentCount[types[i]].length != 0) {
            
            avTypes.push(types[i])
        }
        i = i + 1
    }

    // console.log(indices)

    // if all types are done, exit
    if (avTypes.length == 0) {
        button.setAttribute("onclick", "location.href='completion.html';")
    } 

    else {
        button.setAttribute("onclick", "location.href='" + avTypes[Math.floor(Math.random() * avTypes.length)] + ".html';")
    }



    // if all trials are completed redirect to a completion page
    // if not all the trials are completed, then randomize the remaining trials
}

function updateCount(type) {
    var newCount = JSON.stringify(currentCount)
    localStorage.setItem('trialCount', newCount) 

    // var newCount = JSON.stringify(currentCount)
    // localStorage.setItem('trialCount', newCount)
}

function getRandomAndRemove(arr) {
  const randomIndex = Math.floor(Math.random() * arr.length); // Generate a random index within the array
  const removedElement = arr.splice(randomIndex, 1); // Remove the element at the random index
  return removedElement[0]; // Return the removed element
}

function maybeSwitchElements(element1, element2) {
  if (Math.random() < 0.5) {
    const parent1 = element1.parentNode;
    const sibling1 = element1.nextSibling === element2 ? element1 : element1.nextSibling;
    element2.parentNode.insertBefore(element1, element2);
    parent1.insertBefore(element2, sibling1);
  }
}


