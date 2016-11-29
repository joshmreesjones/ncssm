import java.awt.Graphics2D;
import java.awt.Color;
import java.awt.BasicStroke;

/**
 * <code>DottedLine</code> is a class for drawing lines using {@link Graphics2D}.
 * <code>DottedLine</code> provides control of start and end coordinates of the,
 * line, line color, dash length, and line stroke. Margins are automatically
 * calculated before the line is drawn.
 * 
 * <code>DottedLine</code> was written for CS404 at NCSSM.
 * 
 * @author Josh Rees-Jones
 * @version 1.0
 *
 */
public class DottedLine extends Shape {
 private int startX;
 private int startY;
 private int endX;
 private int endY;
 private double dashLength;
 private Color color;
 private BasicStroke stroke;

 private int distX;
 private int distY;
 private double lineLength;

 private final double marginMin = 2.0;
 private int dashes;
 private double marginLength;

 private int dashDistX;
 private int dashDistY;
 private int marginDistX;
 private int marginDistY;
 
 private int dirX;
 private int dirY;

 private int tempStartX;
 private int tempStartY;
 private int tempEndX;
 private int tempEndY;

 private int incrementX;
 private int incrementY;
 
 /**
  * Constructs a new <code>DottedLine</code> object.
  * 
  * @param newStartX the specified x-coordinate of the starting point of the <code>DottedLine</code>
  * @param newStartY the specified y-coordinate of the starting point of the <code>DottedLine</code>
  * @param newEndX the specified x-coordinate of the ending point of the <code>DottedLine</code>
  * @param newEndY the specified y-coordinate of the ending point of the <code>DottedLine</code>
  * @param newDashLength the dash length
  * @param newColor the color of the line
  * @param newStroke the stroke of the line
  */
 public DottedLine(int newStartX, int newStartY, int newEndX, int newEndY, double newDashLength, Color newColor, BasicStroke newStroke) {
  startX = newStartX;
  startY = newStartY;
  endX = newEndX;
  endY = newEndY;
  dashLength = newDashLength;
  color = newColor;
  stroke = newStroke;
  
  distX = endX - startX;
  distY = endY - startY;
  lineLength = Math.sqrt(Math.pow(distX, 2) + Math.pow(distY, 2));
  
  dashes = (int) (lineLength / (dashLength + marginMin));
  marginLength = (lineLength - (dashes * dashLength)) / (dashes - 1);
  
  dashDistX = (int) ((double) distX * (dashLength / lineLength));
  dashDistY = (int) ((double) distY * (dashLength / lineLength));
  marginDistX = (int) ((double) distX * (marginLength / lineLength));
  marginDistY = (int) ((double) distY * (marginLength / lineLength));
  
  dirX = ((endX - startX) > 0) ? 1 : -1;
  dirY = ((endY - startY) > 0) ? 1 : -1;
  
  tempStartX = startX;
  tempStartY = startY;
  tempEndX = tempStartX + dashDistX;
  tempEndY = tempStartY + dashDistY;
  incrementX = dashDistX + marginDistX;
  incrementY = dashDistY + marginDistY;
 }
 
 /**
  * Constructs a new <code>DottedLine</code> object with some default values.
  * 
  * @param newStartX the specified x-coordinate of the starting point of the <code>DottedLine</code>
  * @param newStartY the specified y-coordinate of the starting point of the <code>DottedLine</code>
  * @param newEndX the specified x-coordinate of the ending point of the <code>DottedLine</code>
  * @param newEndY the specified y-coordinate of the ending point of the <code>DottedLine</code>
  * @param newColor the color of the line
  */
 public DottedLine(int newStartX, int newStartY, int newEndX, int newEndY, Color newColor) {
  this(newStartX, newStartY, newEndX, newEndY, 5.0, newColor, new BasicStroke(1.0f));
 }
 
 /**
  * Constructs a new <code>DottedLine</code> object with some default values.
  * 
  * @param newStartX the specified x-coordinate of the starting point of the <code>DottedLine</code>
  * @param newStartY the specified y-coordinate of the starting point of the <code>DottedLine</code>
  * @param newEndX the specified x-coordinate of the ending point of the <code>DottedLine</code>
  * @param newEndY the specified y-coordinate of the ending point of the <code>DottedLine</code>
  * @param newStroke the stroke of the line
  */
 public DottedLine(int newStartX, int newStartY, int newEndX, int newEndY, BasicStroke newStroke) {
  this(newStartX, newStartY, newEndX, newEndY, 5.0, new Color(0, 0, 0), newStroke);
 }
 
 /**
  * Constructs a new <code>DottedLine</code> object with some default values.
  * 
  * @param newStartX the specified x-coordinate of the starting point of the <code>DottedLine</code>
  * @param newStartY the specified y-coordinate of the starting point of the <code>DottedLine</code>
  * @param newEndX the specified x-coordinate of the ending point of the <code>DottedLine</code>
  * @param newEndY the specified y-coordinate of the ending point of the <code>DottedLine</code>
  */
 public DottedLine(int newStartX, int newStartY, int newEndX, int newEndY) {
  this(newStartX, newStartY, newEndX, newEndY, 5.0, new Color(0, 0, 0), new BasicStroke(1.0f));
 }

 /**
  * Constructs a new <code>DottedLine</code> object with all default values.
  */
 public DottedLine() {
  this(0, 0, 1, 1, 5.0, new Color(0, 0, 0), new BasicStroke(1.0f));
 }
 
 /**
  * Paints the <code>DottedLine</code> using the current values of the instance variables.
  * 
  * @param g2d Graphics2D object for painting
  */
 public void drawWith(Graphics2D g2d) {

  g2d.setColor(color);
  g2d.setStroke(stroke);
  
  while ((((endX - tempEndX) * dirX) > 0) && (((endY - tempEndY) * dirY) > 0)) {
   g2d.drawLine(tempStartX, tempStartY, tempEndX, tempEndY);
   
   tempStartX += 2 * incrementX;
   tempStartY += 2 * incrementY;
   tempEndX += 2 * incrementX;
   tempEndY += 2 * incrementY;
  }
  
  System.out.println("Done");
 }
 
 /**
  * Returns the value of the starting x-coordinate of the <code>DottedLine</code>.
  * 
  * @return the value of startX
  */
 public int getStartX() {
  return startX;
 }
 
 /**
  * Returns the value of the starting y-coordinate of the <code>DottedLine</code>.
  * 
  * @return the value of startY
  */
 public int getStartY() {
  return startY;
 }
 
 /**
  * Returns the value of the ending x-coordinate of the <code>DottedLine</code>.
  * 
  * @return the value of endX
  */
 public int getEndX() {
  return endX;
 }
 
 /**
  * Returns the value of the ending y-coordinate of the <code>DottedLine</code>.
  * 
  * @return the value of endY
  */
 public int getEndY() {
  return endY;
 }
 
 /**
  * Returns the value of the total length of the <code>DottedLine</code> from the starting point to the ending point.
  * 
  * @return the value of lineLength
  */
 public double getLineLength() {
  return lineLength;
 }
 
 /**
  * Returns the length of each dash of the <code>DottedLine</code>, specified in an argument in the constructor or with the {@link #setDashLength}
  * 
  * @return the value of dashLength
  */
 public double getDashLength() {
  return dashLength;
 }
 
 /**
  * Returns the length of each margin of the <code>DottedLine</code>, calculated dynamically based on lineLength, dashes, and dashLength. 
  * 
  * @return the value of marginLength
  */
 public double getMarginLength() {
  return marginLength;
 }
 
 /**
  * Returns the number of dashes in the <code>DottedLine</code>.
  * 
  * @return the value of dashes
  */
 public int getDashes() {
  return dashes;
 }
 
 /**
  * Returns the stroke of the <code>DottedLine</code>.
  * 
  * @return the value of stroke
  */
 public BasicStroke getStroke() {
  return stroke;
 }
 
 /**
  * Sets the <code>startX</code> attribute for the <code>DottedLine</code> class.
  * 
  * @param newStartX the value to set <code>startX</code> to
  */
 public void setStartX(int newStartX) {
  startX = newStartX;
 }
 
 /**
  * Sets the <code>startY</code> attribute for the <code>DottedLine</code> class.
  * 
  * @param newStartY the value to set <code>startY</code> to
  */
 public void setStartY(int newStartY) {
  startY = newStartY;
 }
 
 /**
  * Sets the <code>endX</code> attribute for the <code>DottedLine</code> class.
  * 
  * @param newEndX the value to set <code>endX</code> to
  */
 public void setEndX(int newEndX) {
  endX = newEndX;
 }
 
 /**
  * Sets the <code>endY</code> attribute for the <code>DottedLine</code> class.
  * 
  * @param newEndY the value to set <code>endY</code> to
  */
 public void setEndY(int newEndY) {
  endY = newEndY;
 }
 
 /**
  * Sets the <code>dashLength</code> attribute for the <code>DottedLine</code> class.
  * 
  * @param newDashLength the value to set <code>dashLength</code> to
  */
 public void setDashLength(double newDashLength) {
  assert (newDashLength == ((lineLength - 2) / 2)): "New dashLength value too high: " + newDashLength;
  dashLength = newDashLength;
 }
 
 /**
  * Sets the color of the <code>DottedLine</code>.
  * 
  * @param newColor the <code>Color</code> object to set the <code>DottedLine</code> color
  */
 public void setColor(Color newColor) {
  color = newColor;
 }
 
 /**
  * Sets the stroke for the <code>DottedLine</code>.
  * 
  * @param newStroke the <code>BasicStroke</code> object to set the <code>newStroke</code> value of the <code>DottedLine</code>
  */
 public void setStroke(BasicStroke newStroke) {
  stroke = newStroke;
 }
 
 public double getArea() {
   return 0.0;
 }
 
 public double getPerimeter() {
   return lineLength * 2;
 }
 
 public String shapeType() {
   return "DottedLine";
 }
 
 public String attributes() {
   return ("{" + 
           "start: (" + startX + ", " + startY + "); " + 
           "end: (" + endX + ", " + endY + "); " + 
           "dashLength: " + dashLength + "; " + 
           "color: " + color.toString() + "; " + 
           "stroke: " + stroke.toString() + ";" + 
           "}");
 }
}