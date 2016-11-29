package edu.ncssm.cs.jps.controllers;

import java.awt.Cursor;
import java.awt.Image;
import java.awt.Point;
import java.awt.Toolkit;

import javax.swing.event.MouseInputAdapter;

public class Tool extends MouseInputAdapter {
	private final Point hotSpot;
	private final String name;
	private final String cursorImagePath;
	
	Toolkit toolkit;
	
	public Tool(Point hotSpot, String name, String cursorImagePath) {
		toolkit = Toolkit.getDefaultToolkit();
		
		this.hotSpot = hotSpot;
		this.name = name;
		this.cursorImagePath = cursorImagePath;
	}
	
	public Cursor getCursor() {
		Image cursorImage = toolkit.getImage(getClass().getResource(cursorImagePath));
		Cursor cursor = toolkit.createCustomCursor(cursorImage, hotSpot, name);
		
		return cursor;
	}
}