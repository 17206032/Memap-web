// validate username
var username = document.getElementById('usernameval');
username.onblur = function(){
    var usernamedata = document.getElementById('usernameval').value;
    var str = /^[a-zA-Z][a-zA-Z0-9_]{5,14}$/;
    var str2 = /^\w{0,5}$/;
    var str3 = /^[^a-zA-Z][a-zA-Z0-9_]{0,50}$/;
    var str4 = /^\w{16,50}$/;
    var error1 = "Only letter, number and '_' allowed";
    var error2 = "Username should be 6 to 15 digits";
    var error3 = "Need set a username";
    var error4 = "Only letter can be the first digit"
    if (usernamedata == ""){
        document.getElementById('usernameerror').innerText=error3;
        setTimeout("getusernamefocus();",100)
    }else{
        if (!str.test(usernamedata)) {
            if(str3.test(usernamedata)){
                document.getElementById('usernameerror').innerText=error4;
            }else{
                if (str2.test(usernamedata)){
                    document.getElementById('usernameerror').innerText=error2;
                }else{
                    if(str4.test(usernamedata)){
                        document.getElementById('usernameerror').innerText=error2;
                    }else{
                        document.getElementById('usernameerror').innerText=error1;
                    }
                }
            }
            setTimeout("getusernamefocus();",100)
           }else{
            document.getElementById('usernameerror').innerText="";
        }
    }
}

username.onclick = function(){
    document.getElementById('usernameerror2').innerText="";
}

function getusernamefocus() {
    document.getElementById('usernameval').focus();
}

// validate email
// reference line 51, https://blog.csdn.net/weixin_33691700/article/details/93191693
var email = document.getElementById('emailval');
email.onblur = function(){
    var emaildata = document.getElementById('emailval').value;
    var str = /^\w+([-_.]\w+)*@\w+([-_.]\w+)*\.\w+([-_.]\w+)*$/;
    var str2 = /^\w+([-_.]\w+)*$/;
    var str3 = /^\w+([-_.]\w+)*@\w+([-_.]\w+)*$/;
    var str4 = /^\w+([-_.]\w+)*@\w+([-_.])*$/;
    var error1 = "Only letter, number and '@ _ . -' allowed";
    var error2 = "Need set an email";
    var error3 = "Wrong email format";
    if (emaildata == ""){
        document.getElementById('emailerror').innerText=error2;
    }else{
        if (!str.test(emaildata)) {
            if (str2.test(emaildata) || str3.test(emaildata) || str4.test(emaildata)){
                document.getElementById('emailerror').innerText=error3;	
            }else{
                document.getElementById('emailerror').innerText=error1;
            }
            setTimeout("getemailfocus();",100)
           }else{
            document.getElementById('emailerror').innerText="";
        }
    }
}

email.onclick = function(){
    document.getElementById('emailerror2').innerText="";
}

function getemailfocus() {
    document.getElementById('emailval').focus();
}

// validate first password
var password1 = document.getElementById('passwordval1');
password1.onblur = function(){
    var password1data = document.getElementById('passwordval1').value;
    var str = /[a-zA-Z0-9_]{6,18}$/;
    var str2 = /^\w{0,5}$/;
    var str3 = /^\w{19,50}$/;
    var error1 = "Only letter, number and '_' allowed";
    var error2 = "Password should be 6 to 18 digits";
    var error3 = "Need set a password";
    if (password1data == ""){
        document.getElementById('password1error').innerText=error3;
    }else{
        if (!str.test(password1data)) {
            if(str2.test(password1data) || str3.test(password1data)){
                document.getElementById('password1error').innerText=error2;
            }else{
                document.getElementById('password1error').innerText=error1;
            }
            setTimeout("getpassword1focus();",100)
           }else{
            document.getElementById('password1error').innerText="";
        }
    }
}

password1.onclick = function(){
    document.getElementById('password1error2').innerText="";
}

function getpassword1focus() {
    document.getElementById('passwordval1').focus();
}

// validate repeated password
var password2 = document.getElementById('passwordval2');
password2.onblur = function(){
    var password2data = document.getElementById('passwordval2').value;
    var password1data = document.getElementById('passwordval1').value; 
    var error1 = "Repeated password is not match with the first";
    var error2 = "Need set a password";
    if (password2data == ""){
        document.getElementById('password2error').innerText=error2;
    }else{
        if (password1data != password2data) {
            document.getElementById('password2error').innerText=error1;
            setTimeout("getpassword2focus();",100)
           }else{
            document.getElementById('password2error').innerText="";
        }
    }
}

password2.onclick = function(){
    document.getElementById('password2error2').innerText="";
}

function getpassword2focus() {
    document.getElementById('passwordval2').focus();
}
