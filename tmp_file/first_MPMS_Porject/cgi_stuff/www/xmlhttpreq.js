/*
 *http://blog.chinaunix.net/uid-28264320-id-4013835.html
 *create items
 */
function createXHR() 
{
    var xhr;


    try 
    {
        xhr = new ActiveXObject("Msxml2.XMLHTTP");
    } 
    catch (e) 
    {
        try 
        {
            xhr = new ActiveXObject("Microsoft.XMLHTTP");
        }
        catch(E) 
        {
            xhr = false;
        }
    }

    if (!xhr && typeof XMLHttpRequest != 'undefined') 
    {
        xhr = new XMLHttpRequest();
    }

    return xhr;
}

/*
 *
 */
function sender() 
{
    xhr = createXHR();

    if(xhr)
    {
        xhr.onreadystatechange=callbackFunction;
    

        //test.cgi
        xhr.open("GET", "/cgi-bin/mpms.cgi?cur_time=" + new Date().getTime());
    
        xhr.send(null);
    }
    else
    {
        //XMLHttpRequest
        alert("Broswer not support!");
    }
}

function updateTimer()
{
    sender();
    setTimeout("updateTimer()", 1000);
}

/*
 *Handle function
 */
function callbackFunction()
{
    if (xhr.readyState == 4) 
    {
        if (xhr.status == 200) 
        {
            var returnValue = xhr.responseText;

            if(returnValue != null && returnValue.length > 0)
            {
                //document.getElementById("current_time").innerHTML = returnValue;
                document.getElementById("current_people").innerHTML = returnValue;
            }
            else
            {
                alert("Result is invail");
            }
        } 
        else 
        {
            alert("Page is not right!");
        }
    }
}

