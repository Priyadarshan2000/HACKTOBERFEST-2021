console.log(`NumbNotes`);
showNotes();
//if user adds a note add to a local storage.
let addBtn = document.getElementById(`addBtn`);
addBtn.addEventListener(`click`, function () {
    let addTxt = document.getElementById(`textArea`);
    let addTitle = document.getElementById(`addTitle`);
    let addDate = document.getElementById(`addDate`);
    let notes = localStorage.getItem("notes");
    if (notes == null) {
        notesObj = [];
    }
    else {
        notesObj = JSON.parse(notes);
    }
    dataObj = {
        title: addTitle.value,
        date: addDate.value,
        text: addTxt.value
    };
    notesObj.push(dataObj);
    localStorage.setItem(`notes`, JSON.stringify(notesObj));
    addTxt.value = "";
    addTitle.value = "";
    addDate.value = "";
    // console.log(notes);
    showNotes();
})

//function to show notes.
function showNotes() {
    let notes = localStorage.getItem(`notes`);
    if (notes == null) {
        notesObj = [];
    }
    else {
        notesObj = JSON.parse(notes);
    }
    let html = "";
    notesObj.forEach(function (element, index) {
        html += `
        <div class="noteCard my-2 mx-2 card" style="width: 18rem;">
            <div class="card-body">
                <h5 class="card-title">${element.title} Date:-${element.date}</h5>
                <p class="card-text">${element.text}</p>
                <button id="${index}" onclick="deleteNote(this.id)"class="btn btn-primary">Delete</button>
            </div>
        </div>`;
    });
    let notesElem = document.getElementById(`notes`);
    if (notesObj.length != 0) {
        notesElem.innerHTML = html;
    }
    else {
        notesElem.innerHTML = `Nothing to show! Add new notes from above section.`;
    }
}

//function to delete notes.
function deleteNote(index) {
    // console.log(`Deleting...`, index+1);
    let notes = localStorage.getItem(`notes`);
    if (notes == null) {
        notesObj = [];
    }
    else {
        notesObj = JSON.parse(notes);
    }
    notesObj.splice(index, 1);
    localStorage.setItem(`notes`, JSON.stringify(notesObj));
    showNotes();
}

let search = document.getElementById('searchText');
search.addEventListener("input", function () {

    let inputVal = search.value;
    // console.log('Input event fired!', inputVal);
    let noteCards = document.getElementsByClassName('noteCard');
    Array.from(noteCards).forEach(function (element) {
        let cardTxt = element.getElementsByTagName("p")[0].innerText;
        if (cardTxt.includes(inputVal)) {
            element.style.display = "block";
        }
        else {
            element.style.display = "none";
        }
        // console.log(cardTxt);
    })
})