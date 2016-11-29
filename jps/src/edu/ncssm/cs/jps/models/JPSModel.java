package edu.ncssm.cs.jps.models;

import java.util.ArrayList;

import edu.ncssm.cs.jps.controllers.ToolController;

public class JPSModel {
	private ArrayList<DocumentModel> documents = new ArrayList<DocumentModel>();
	
	private ToolController currentTool;
	
	public void addDocument(DocumentModel document) {
		documents.add(document);
	}
	
	public ToolController getCurrentTool() {
		return currentTool;
	}
	
	public void setCurrentTool(ToolController currentTool) {
		this.currentTool = currentTool;
	}
}