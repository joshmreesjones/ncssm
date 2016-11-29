package edu.ncssm.cs.jps.models;

import java.awt.image.BufferedImage;
import java.util.ArrayList;

public class DocumentModel {
	private ArrayList<BufferedImage> layers = new ArrayList<BufferedImage>();
	
	private int imageWidth;
	private int imageHeight;
	
	private String path;
	private String title;
	
	public DocumentModel(BufferedImage firstLayer, String path, String title) {
		this.path = path;
		this.title = title;
		
		imageWidth = firstLayer.getWidth();
		imageHeight = firstLayer.getHeight();
		
		addLayer(firstLayer);
	}
	
	public void addLayer(BufferedImage layer) {
		layers.add(layer);
	}
	
	public int getImageWidth() {
		return imageWidth;
	}
	
	public int getImageHeight() {
		return imageHeight;
	}
	
	public ArrayList<BufferedImage> getLayers() {
		return layers;
	}
	
	public String getPath() {
		return path;
	}
	
	public String getTitle() {
		return title;
	}
}