setInterval(followandscroll, 100);
var x = document.getElementsByClassName("button button--primary button--small u-noUserSelect button--withChrome button--follow js-followButton");
var i = 0;
function followandscroll(){
    if(i<x.length){
        if(!((x[i].className).indexOf('is-active') > -1)){
            x[i].click();
        }
        i++;
    }else{
        window.scrollTo(0,document.body.scrollHeight);
        x = document.getElementsByClassName("button button--primary button--small u-noUserSelect button--withChrome button--follow js-followButton");
    }
}