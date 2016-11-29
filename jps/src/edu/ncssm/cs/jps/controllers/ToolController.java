package edu.ncssm.cs.jps.controllers;

import java.awt.Cursor;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.awt.event.MouseWheelListener;

public interface ToolController extends MouseListener, MouseMotionListener, MouseWheelListener {
	public Cursor getCursor();
}