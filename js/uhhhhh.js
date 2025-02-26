//things you put in <head> (css and title)
var title = document.createElement('title');
title.textContent = "uhhhh";
document.head.appendChild(title);

var css = document.createElement('style');
css.innerHTML = `
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

* {
font-family: "Roboto", serif;
  font-weight: 400;
  font-style: normal;
  font-variation-settings:
    "wdth" 100;

    }

body {
display:flex;
align-items:center;
justify-content:center;
min-height: 100vh;
margin:0;
padding:0;
}

#username-box {
height: 80%;
width: 90%;
background-color: rgb(248, 190, 0);
border: none;
resize: none;
}

#username-div {
background-color: rgb(248, 190, 0);
    height: 200px;
    text-align: center;
    width: 100%;
    border-radius: 4px;
    color: rgb(0, 0, 0);
    margin-top: 10px;
    box-shadow: 0 0 10px black;
    transition: .3s ease;
    }

    #username-div:hover {
    transform: translateY(-5px);
    }

    #username-container {
    max-width:300px;
    display:flex;
    flex-wrap:wrap;
    }

    #username {
    width:100px;
    display:flex;
    flex-wrap:wrap;
    }
`;

document.head.appendChild(css);

//body
var div = document.createElement('div');


div.innerHTML = `<h1><strong>uhhhhhhhhhhhhhhhh</strong></h1>
<h3>yeah i have no clue what to say LMAO</h3>
<p>put your username here or smth</p>
<div id="username-container">
<div id="username-div">
Sticky note
<textarea id="username-box" placeholder="Enter your username here!"></textarea>
</div>
</div>`;

document.body.appendChild(div);

var username = document.querySelector('#username-box');
var usernameContainer = document.querySelector('#username-container')

username.addEventListener("input", sayHiorSmth);

var sayHi = document.createElement('p');
sayHi.id = 'username';

function sayHiorSmth() {
    sayHi.textContent = `Hi, ${username.value}!`;
}

usernameContainer.appendChild(sayHi);