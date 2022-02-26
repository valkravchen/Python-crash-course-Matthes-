function testSize(num) {
    // Only change code below this line
  if (num < 5) {
    num = 'Tiny';
  } else if (num < 10) {
    num = 'Small';
  } else if (num < 15) {
    num = 'Medium';
  } else if (num < 20) {
    num = 'Large';
  } else{
    num = 'Huge';
  }
  return num;
  
  
    // Only change code above this line
  }
  
  testSize(7);