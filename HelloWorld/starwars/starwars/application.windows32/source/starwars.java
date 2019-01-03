import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class starwars extends PApplet {

String txt;
float y =0;

public void setup(){
  
 
  String[] lines = loadStrings("space.txt");
  txt = join(lines,'\n');
  y = height;
}
public void draw(){
  background(0);

  fill(75,213,238);
  textSize(25);
  textAlign(CENTER);
  rotateX(PI/4);
  text(txt,0,y,width,height*2);
  y=y-0.3f;
}
  public void settings() {  size(800,600,P3D); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "starwars" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
