package edu.ncssm.cs.jps.controllers.tools;

import java.awt.Point;
import java.awt.event.MouseEvent;

import edu.ncssm.cs.jps.controllers.Tool;
import edu.ncssm.cs.jps.controllers.ToolController;
import edu.ncssm.cs.jps.views.JPSView;

public class PanTool extends Tool implements ToolController {
	private final JPSView view;
	
	private int mouseX;
	private int mouseY;
	
	public PanTool(JPSView view) {
		super(new Point(3, 2), "panTool", "/res/panToolCursor.png");
		
		this.view = view;
	}

	@Override
	public void mouseDragged(MouseEvent event) {
		int changeX = event.getX() - mouseX;
		int changeY = event.getY() - mouseY;
		
		view.setRenderPositionX(view.getRenderPositionX() + changeX);
		view.setRenderPositionY(view.getRenderPositionY() + changeY);
		
		mouseX = event.getX();
		mouseY = event.getY();
		
		view.repaintCanvasPanelView();
	}
	
	@Override
	public void mousePressed(MouseEvent event) {
		this.mouseX = event.getX();
		this.mouseY = event.getY();
	}
}