let totalImages = 6;
let currentImage = 1;
let table_nums = [[52.5, 95.4], [33.9, 75.4], [24.2, 6.1], [36.7, 56.4], [67.3, 89.7], [53.0, 18.6]]
let ordering = [3, 2, 0, 4, 6, 5, 1]

// const sortedList = table_nums.sort((a, b) => {
//     const indexA = table_nums.indexOf(a);
//     const indexB = table_nums.indexOf(b);
//     return ordering.indexOf(indexA) - ordering.indexOf(indexB);
//   });

// Generate the HTML code for each image container
let imageContainers = "";

for (let i = 0; i < totalImages; i++) {
    imageContainers += `
    <div id="image-container-${i + 1}" class="image-container">
        <table style="width:12cm;height:6cm;">
            <tr>
                <th scope="col" style="font-weight: bold;">${(table_nums[i])[0].toFixed(1)}</th>
                <th scope="col" style="font-weight: bold;">${(table_nums[i])[1].toFixed(1)}</th>
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
        document.getElementById('trial-button').setAttribute("onclick", "window.location.href = 'index.html';")
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
        document.getElementById('trial-button').setAttribute("onclick", "window.location.href = 'index.html';")
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
