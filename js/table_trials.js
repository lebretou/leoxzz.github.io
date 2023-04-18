let totalImages = 7;
let currentImage = 1;
let table_nums = [[23.8, 79.2], [46.5, 18.6], [86.1, 43.1], [28.9, 48.2],[64.6, 92.3],[24.3, 30.3],[12.7, 63.6]]
let ordering = [3, 2, 0, 4, 6, 5, 1]

const sortedList = table_nums.sort((a, b) => {
    const indexA = table_nums.indexOf(a);
    const indexB = table_nums.indexOf(b);
    return ordering.indexOf(indexA) - ordering.indexOf(indexB);
  });

// Generate the HTML code for each image container
let imageContainers = "";

for (let i = 0; i < totalImages; i++) {
    imageContainers += `
    <div id="image-container-${i + 1}" class="image-container">
        <table style="width:12cm;height:6cm;">
            <tr>
                <th scope="col" style="font-weight: bold;">${(sortedList[i])[0]}</th>
                <th scope="col" style="font-weight: bold;">${(sortedList[i])[1]}</th>
            </tr>

        </table>
    </div>
    `;
    
    // Add the image containers to the DOM
    document.getElementById("image-container").innerHTML = imageContainers;
    document.getElementById(`image-container-${currentImage}`).style.display = "block";

    // Update the progress bar
    const progress = (currentImage / totalImages) * 100;
    document.querySelector('.progress').style.width = `${progress}%`;
}


function showNextImage() {
    // Hide the current image container
    document.getElementById(`image-container-${currentImage}`).style.display = "none";

    // Increment the current image counter
    currentImage++;

    console.log(currentImage + "/" + totalImages)

    // If we have reached the end, redirect to the completion page
    if (currentImage == totalImages) {
        document.getElementById('trial-button').setAttribute("onclick", "window.location.href = 'trans.html';")
    }

    // Show the next image container
    document.getElementById(`image-container-${currentImage}`).style.display = "block";

    // Update the progress bar
    const progress = (currentImage / totalImages) * 100;
    document.querySelector('.progress').style.width = `${progress}%`;

    if (currentImage > 1) {
        document.getElementById(`p-button`).disabled = false;
    }
}

function showLastImage() {
    // Hide the current image container
    document.getElementById(`image-container-${currentImage}`).style.display = "none";

    // Increment the current image counter
    currentImage--;

    console.log(currentImage + "/" + totalImages)

    // If we have reached the end, redirect to the completion page
    if (currentImage == totalImages) {
        document.getElementById('trial-button').setAttribute("onclick", "window.location.href = 'trans.html';")
    }

    // Show the next image container
    document.getElementById(`image-container-${currentImage}`).style.display = "block";

    if (currentImage != totalImages) {
        document.getElementById('trial-button').setAttribute("onclick", "showNextImage()")
    }

    // Update the progress bar
    const progress = (currentImage / totalImages) * 100;
    document.querySelector('.progress').style.width = `${progress}%`;

    if (currentImage == 1) {
        document.getElementById(`p-button`).disabled = true;
    }
}
