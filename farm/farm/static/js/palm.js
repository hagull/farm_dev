

function m_btn(){
  var c_nav = document.getElementsByClassName('control-nav');
  var m_nav = document.getElementsByClassName('mobile_nav');
  var value = "off";
  if( this.value == 'off') {
    this.value = 'on';
    c_nav[0].style.display = 'none';
    c_nav[0].style.zIndex = '1002';
  } else {
    this.value='off';
    c_nav[0].style.display = 'block';
    c_nav[0].style.zIndex = '3';
  }

}
