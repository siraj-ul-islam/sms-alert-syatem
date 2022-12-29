// Optional
Prism.plugins.NormalizeWhitespace.setDefaults({
  'remove-trailing': true,
  'remove-indent': true,
  'left-trim': true,
  'right-trim': true,
  });
// choices search for country
let choices = new Choices(document.querySelector("#choices-country"), {
    placeholder: true,
    searchPlaceholderValue: "Search",
    itemSelectText: "Select",
});
// choices search for state
let choiceState = new Choices(document.querySelector("#choices-state"), {
    placeholder: true,
    searchPlaceholderValue: "Search",
    itemSelectText: "Select",
});
    let wildCard = new Choices(document.getElementById("wildCard"), {
    delimiter: "/n",
    editItems: true,
    maxItemCount: 5,
    removeItemButton: true,
});
let directUrl = new Choices(document.getElementById("directUrl"), {
    delimiter: "/n",
    editItems: true,
    maxItemCount: 5,
    removeItemButton: true,
});

let tierTwoUrl = new Choices(document.getElementById("tierTwoUrl"), {
    delimiter: "/n",
    editItems: true,
    maxItemCount: 5,
    removeItemButton: true,
});

let keywordModifier = new Choices(document.getElementById("keywordModifier"), {
    delimiter: "/n",
    editItems: true,
    maxItemCount: 5,
    removeItemButton: true,
});

let tierOneUrl = new Choices(document.getElementById("tierOneUrl"), {
    delimiter: "/n",
    editItems: true,
    maxItemCount: 5,
    removeItemButton: true,
});

let destinationUrl = new Choices(document.getElementById("destinationUrl"), {
    delimiter: "/n",
    editItems: true,
    maxItemCount: 5,
    removeItemButton: true,
});
