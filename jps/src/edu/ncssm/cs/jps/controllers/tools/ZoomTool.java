package edu.ncssm.cs.jps.controllers.tools;

import java.awt.Point;
import java.awt.event.MouseEvent;

import edu.ncssm.cs.jps.controllers.Tool;
import edu.ncssm.cs.jps.controllers.ToolController;
import edu.ncssm.cs.jps.views.JPSView;

public class ZoomTool extends Tool implements ToolController {
	private final JPSView view;
	
	private final double zoomChangeFactor = 0.01;
	
	private int initialX;
	private int initialY;
	
	private int lastX;
	
	public ZoomTool(JPSView view) {
		super(new Point(6, 6), "zoomTool", "/res/zoomToolCursor.png");
		
		this.view = view;
	}
	
	@Override
	public void mouseClicked(MouseEvent event) {
		view.zoomInAround(event.getX(), event.getY());
	}
	
	@Override
	public void mousePressed(MouseEvent event) {
		initialX = event.getX();
		initialY = event.getY();
		
		lastX = event.getX();
	}
	
	@Override
	public void mouseDragged(MouseEvent event) {
		int changeX = event.getX() - lastX;
		
		if (changeX > 0) {
			view.zoomInAround(initialX, initialY, zoomChangeFactor * Math.abs(changeX));
		} else if (changeX < 0) {
			view.zoomOutAround(initialX, initialY, zoomChangeFactor * Math.abs(changeX));
		}
		
		lastX = event.getX();
	}
}