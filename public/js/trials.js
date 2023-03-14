let totalImages = 0;
let currentImage = 1;
let table_nums = [[12.2, 47.0], [27.8, 81.8], [96.4, 40.5], [51.9, 26.0], [83.6, 48.5], [38.6, 58.6], [4.6, 3.4], [55.7, 67.9]]



// Load the SVG file names from the text file
fetch("js/svg_paths.txt")
    .then(response => response.text())
    .then(data => {
        // Split the text file contents into an array of image names
        imageNames = data.trim().split("\n");
        shuffleArray(imageNames)
        totalImages = imageNames.length;
        random_indices = generateIntegers()

        // Generate the HTML code for each image container
        let imageContainers = "";
        let j = 0
        let table_i = 0
        for (let i = 0; i < totalImages; i++) {
            imageContainers += `<div id="image-container-${j + 1}" class="image-container">
                              <object data="${imageNames[i]}" type="image/svg+xml"></object>
                           </div>`;
            j += 1;

            // randomly insert tables into the trials
            if (random_indices.includes(i)) {
                imageContainers += `
                <div id="image-container-${j + 1}" class="image-container">
                    <table style="width:12cm;height:6cm;">
                        <tr>
                            <th scope="col" style="font-weight: bold;">Encoding</th>
                            <th scope="col" style="font-weight: bold;">Value</th>
                        </tr>

                        <tr>
                            <th scope="row">A</th>
                            <th>${(table_nums[table_i])[0]}</th>
                        </tr>

                        <tr>
                            <th scope="row">B</th>
                            <th>${(table_nums[table_i])[1]}</th>
                        </tr>
                    </table>
                </div>
                `;
                table_i += 1
                j += 1
            }
        }


        // Add the image containers to the DOM
        document.getElementById("image-container").innerHTML = imageContainers;
        document.getElementById(`image-container-${currentImage}`).style.display = "block";

        totalImages += 8
    });

function showNextImage() {
    // Hide the current image container
    document.getElementById(`image-container-${currentImage}`).style.display = "none";

    // Increment the current image counter
    currentImage++;

    console.log(currentImage + "/" + totalImages)

    // If we have reached the end, redirect to the completion page
    if (currentImage == totalImages) {
        document.getElementById('trial-button').setAttribute("onclick", "window.location.href = 'completion.html';")
    }

    // Show the next image container
    document.getElementById(`image-container-${currentImage}`).style.display = "block";

    // Update the progress bar
    const progress = (currentImage / totalImages) * 100;
    document.querySelector('.progress').style.width = `${progress}%`;
}

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}


function generateIntegers() {
    const integers = [];
    while (integers.length < 8) {
        const integer = Math.floor(Math.random() * 56);
        if (integer > 0 && !integers.includes(integer)) {
            integers.push(integer);
        }
    }
    return integers;
}

function generate_pairs(ratios) {
    let pairs = []

    for (let i = 0; i < ratios.length; i++) {
        let larger_num = Math.random() * 100
        let smaller_num = larger_num * ratios[i]
        larger_num = larger_num.toFixed(1)
        smaller_num = smaller_num.toFixed(1)

        let coin_flip = Math.floor(Math.random() * 1)
        if (coin_flip == 0) {
            let tmp = larger_num
            larger_num = smaller_num
            smaller_num = tmp
        }
        pairs.push([larger_num, smaller_num])
    }

     return pairs
}
