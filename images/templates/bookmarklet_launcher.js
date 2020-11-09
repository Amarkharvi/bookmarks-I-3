(function(){
    if(window.myBookmarklet !== undefined){
        myBookmarklet();
    }
    else{
        document.body.appendChild(document.createElement('script')).src='http://a15b8dcb95f0.ngrok.io/static/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999)
    }
})();