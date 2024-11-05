console.log("connected");

let cardCollection = document.getElementById("card-collection");

function addCard(cardData) {
  let newCard = document.createElement("div");
  newCard.classList.add("card");

  //card
  let cardName = document.createElement("h3");
  let cardHp = document.createElement("h4");
  let cardElement = document.createElement("h4");
  let cardMove = document.createElement("h5");
  let cardDescription = document.createElement("p");

  cardName.textContent = `Name: ${cardData.name}`;
  cardHp.textContent = `Hp: ${cardData.hp}`;
  cardElement.textContent = `Type: ${cardData.element}`;
  cardMove.textContent = `Move: ${cardData.move}`;
  cardDescription.textContent = `Description: ${cardData.description}`;

  newCard.appendChild(cardName);
  newCard.appendChild(cardHp);
  newCard.appendChild(cardElement);
  newCard.appendChild(cardMove);
  newCard.appendChild(cardDescription);
  //comment

  //update
  let updateButton = document.createElement("button");
  updateButton.textContent = "Update";
  updateButton.id = "update-button";
  updateButton.onclick = () => populateUpdateForm(cardData); //updateCard(cardData.id);

  newCard.appendChild(updateButton);

  //delete
  let deleteButton = document.createElement("button");
  deleteButton.textContent = "Delete";
  deleteButton.id = "delete-button";
  deleteButton.onclick = () => confirmDelete(cardData.id); //deleteCard(cardData.id);

  newCard.appendChild(deleteButton);

  cardCollection.prepend(newCard);
}
//populates
function populateUpdateForm(cardData) {
  // Fill the fields so you can edit
  document.querySelector("#input-name").value = cardData.name;
  document.querySelector("#input-hp").value = cardData.hp;
  document.querySelector("#input-element").value = cardData.element;
  document.querySelector("#input-move").value = cardData.move;
  document.querySelector("#input-description").value = cardData.description;

  //Change the button text to update card
  addCardButton.textContent = "Update Card";
  addCardButton.onclick = () => updateCard(cardData.id);
}
//deleteConfirmation

function confirmDelete(pokemon_id) {
  if (confirm("Are you sure you wish to delete this card?")) {
    deleteCard(pokemon_id);
  }
}

function loadCardsFromServer() {
  fetch("http://localhost:8080/pokemons").then(function (response) {
    response.json().then(function (data) {
      console.log(data);
      let cards = data;
      cardCollection.textContent = "";
      cards.forEach(addCard);
    });
  });
}

let addCardButton = document.querySelector("#add-button");
function addNewCard() {
  console.log("button clicked");
  let inputCardName = document.querySelector("#input-name");
  let inputCardHp = document.querySelector("#input-hp");
  let inputCardElement = document.querySelector("#input-element");
  let inputCardMove = document.querySelector("#input-move");
  let inputCardDescription = document.querySelector("#input-description");

  console.log(
    inputCardName.value,
    inputCardHp,
    inputCardElement,
    inputCardMove,
    inputCardDescription
  );
  //prep data to send to server
  let data = "name=" + encodeURIComponent(inputCardName.value);
  data += "&hp=" + encodeURIComponent(inputCardHp.value);
  data += "&element=" + encodeURIComponent(inputCardElement.value);
  data += "&move=" + encodeURIComponent(inputCardMove.value);
  data += "&description=" + encodeURIComponent(inputCardDescription.value);
  // name=Tatsu&review=Best%20Flying%20Coaster
  //send new review value to the serer
  fetch("http://localhost:8080/pokemons", {
    method: "POST",
    body: data,
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  }).then(function (response) {
    console.log("new card created!", response);
    cardCollection.textContent = "";
    loadCardsFromServer();
  });
}

function updateCard(pokemon_id) {
  let name = document.querySelector("#input-name").value;
  let hp = document.querySelector("#input-hp").value;
  let element = document.querySelector("#input-element").value;
  let move = document.querySelector("#input-move").value;
  let description = document.querySelector("#input-description").value;

  let data = `name=${encodeURIComponent(name)}&hp=${encodeURIComponent(
    hp
  )}&element=${encodeURIComponent(element)}&move=${encodeURIComponent(
    move
  )}&description=${encodeURIComponent(description)}`;

  fetch(`http://localhost:8080/pokemons/${pokemon_id}`, {
    method: "PUT",
    body: data,
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  }).then((response) => {
    console.log(`Card ${pokemon_id} updated`, response);
    loadCardsFromServer();
  });
}

// Delete a Pokémon card
function deleteCard(pokemon_id) {
  fetch(`http://localhost:8080/pokemons/${pokemon_id}`, {
    method: "DELETE",
  }).then((response) => {
    console.log(`Card ${pokemon_id} deleted!`, response);
    loadCardsFromServer();
  });
}
function resetForm() {
  document.querySelector("#input-name").value = "";
  document.querySelector("#input-hp").value = "";
  document.querySelector("#input-element").value = "";
  document.querySelector("#input-move").value = "";
  document.querySelector("#input-description").value = "";
  addCardButton.textContent = "Add a Card";
  addCardButton.onclick = addNewCard; // Reset button function
}

addCardButton.onclick = addNewCard;
loadCardsFromServer();
