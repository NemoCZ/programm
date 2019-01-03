String txt;
float y =0;

void setup(){
  size(800,600,P3D);
 
  String[] lines = loadStrings("space.txt");
  txt = join(lines,'\n');
  y = height;
}
void draw(){
  background(0);

  fill(75,213,238);
  textSize(25);
  textAlign(CENTER);
  rotateX(PI/4);
  text(txt,0,y,width,height*2);
  y=y-0.3;
}