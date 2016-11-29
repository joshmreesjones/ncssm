package edu.ncssm.cs.jps.views;

import java.awt.Graphics;
import java.awt.image.BufferedImage;

import javax.swing.JPanel;

import edu.ncssm.cs.jps.models.DocumentModel;

@SuppressWarnings("serial")
public class CanvasPanelView extends JPanel {
	private DocumentModel document;

	private double zoomFactor;
	private final double zoomChangeFactor = .25;
	private final double minimumZoomFactor = .00125;
	private final double maximumZoomFactor = 32;
	
	private int renderPositionX;
	private int renderPositionY;

	private final int margin = 75;
	private final int zoomFitMargin = 25;

	private int sourceX1;
	private int sourceY1;
	private int sourceX2;
	private int sourceY2;
	private int destinationX1;
	private int destinationY1;
	private int destinationX2;
	private int destinationY2;

	@Override
	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		
		setRenderValues();

		for (BufferedImage layer : document.getLayers()) {
			g.drawImage(layer, destinationX1, destinationY1, destinationX2,
					destinationY2, sourceX1, sourceY1, sourceX2, sourceY2, null);
		}
	}
	
	private void setRenderValues() {
		int canvasPanelWidth = this.getWidth();
		int canvasPanelHeight = this.getHeight();

		int imageWidth = document.getImageWidth();
		int imageHeight = document.getImageHeight();

		int scaledImageWidth = (int) (zoomFactor * imageWidth);
		int scaledImageHeight = (int) (zoomFactor * imageHeight);

		if ((renderPositionX < (margin - scaledImageWidth))
				&& (canvasPanelWidth > margin)) {
			if (scaledImageWidth > margin) {
				renderPositionX = margin - scaledImageWidth;
			} else if (renderPositionX < 0) {
				renderPositionX = 0;
			}
		} else if ((renderPositionX > (canvasPanelWidth - margin))
				&& (canvasPanelWidth > margin)) {
			if (scaledImageWidth > margin) {
				renderPositionX = canvasPanelWidth - margin;
			} else if (renderPositionX + scaledImageWidth > canvasPanelWidth) {
				renderPositionX = canvasPanelWidth - scaledImageWidth;
			}
		}

		if ((renderPositionY < (margin - scaledImageHeight))
				&& (canvasPanelHeight > margin)) {
			if (scaledImageHeight > margin) {
				renderPositionY = margin - scaledImageHeight;
			} else if (renderPositionY < 0) {
				renderPositionY = 0;
			}
		} else if ((renderPositionY > (canvasPanelHeight - margin))
				&& (canvasPanelHeight > margin)) {
			if (scaledImageHeight > margin) {
				renderPositionY = canvasPanelHeight - margin;
			} else if (renderPositionY + scaledImageHeight > canvasPanelHeight) {
				renderPositionY = canvasPanelHeight - scaledImageHeight;
			}
		}

		destinationX1 = renderPositionX;
		destinationY1 = renderPositionY;
		destinationX2 = renderPositionX + scaledImageWidth;
		destinationY2 = renderPositionY + scaledImageHeight;
		sourceX1 = 0;
		sourceY1 = 0;
		sourceX2 = imageWidth;
		sourceY2 = imageHeight;
	}
	
	public void setDocument(DocumentModel document) {
		this.document = document;
	}

	public double calculateZoomFit() {
		int canvasWidth = this.getWidth();
		int canvasHeight = this.getHeight();

		int imageWidth = document.getImageWidth();
		int imageHeight = document.getImageHeight();

		double imageAspectRatio = ((double) imageWidth - (zoomFitMargin * 2))
				/ ((double) imageHeight - (zoomFitMargin * 2));
		double canvasAspectRatio = (double) canvasWidth / canvasHeight;

		if (imageAspectRatio < canvasAspectRatio) {
			return ((double) canvasHeight - (zoomFitMargin * 2)) / imageHeight;
		} else
			return ((double) canvasWidth - (zoomFitMargin * 2)) / imageWidth;
	}

	public double getMaximumZoomFactor() {
		return maximumZoomFactor;
	}

	public double getMinimumZoomFactor() {
		return minimumZoomFactor;
	}
	
	public int getRenderPositionX() {
		return renderPositionX;
	}
	
	public int getRenderPositionY() {
		return renderPositionY;
	}
	
	public double getZoomChangeFactor() {
		return zoomChangeFactor;
	}
	
	public double getZoomFactor() {
		return zoomFactor;
	}

	public void setRenderPositionX(int renderPositionX) {
		this.renderPositionX = renderPositionX;
	}
	
	public void setRenderPositionY(int renderPositionY) {
		this.renderPositionY = renderPositionY;
	}
	
	public void setZoomActualPixels() {
		if (zoomFactor > 1) {
			zoomOutAround(this.getWidth() / 2, this.getHeight() / 2, 1 / zoomFactor);
		} else if (zoomFactor < 1) {
			zoomInAround(this.getWidth() / 2, this.getHeight() / 2, 1 / zoomFactor);
		}
		
		repaint();
	}
	
	public void setZoomFactor(double zoomFactor) {
		if (zoomFactor < minimumZoomFactor) {
			this.zoomFactor = minimumZoomFactor;
		} else if (zoomFactor > maximumZoomFactor) {
			this.zoomFactor = maximumZoomFactor;
		} else {
			this.zoomFactor = zoomFactor;
		}

		repaint();
	}
	
	public void setZoomFactorAround(int centerX, int centerY, double zoomFactor) {
		if (this.zoomFactor > zoomFactor) {
			zoomOutAround(centerX, centerY, zoomFactor / this.zoomFactor);
		} else if (this.zoomFactor < zoomFactor) {
			zoomInAround(centerX, centerY, zoomFactor / this.zoomFactor);
		}
	}
	
	public void setZoomFit() {
		setZoomFactor(calculateZoomFit());

		renderPositionX = (int) ((this.getWidth() - (zoomFactor * document.getImageWidth())) / 2);
		renderPositionY = (int) ((this.getHeight() - (zoomFactor * document.getImageHeight())) / 2);

		repaint();
	}
	
	public void zoomIn() {
		zoomInAround(this.getWidth() / 2, this.getHeight() / 2, 1 + zoomChangeFactor);
	}
	
	public void zoomInAround(int centerX, int centerY, double zoomChangeFactor) {
		if (zoomFactor >= maximumZoomFactor) {
			zoomFactor = maximumZoomFactor;
		} else if (zoomFactor * zoomChangeFactor >= maximumZoomFactor) {
			renderPositionX = (int) (centerX - ((centerX - renderPositionX) * (maximumZoomFactor / zoomFactor)));
			renderPositionY = (int) (centerY - ((centerY - renderPositionY) * (maximumZoomFactor / zoomFactor)));
			
			zoomFactor = maximumZoomFactor;
		} else {
			renderPositionX = (int) (centerX - ((centerX - renderPositionX) * zoomChangeFactor));
			renderPositionY = (int) (centerY - ((centerY - renderPositionY) * zoomChangeFactor));
			
			zoomFactor *= zoomChangeFactor;
		}
		
		repaint();
	}
	
	public void zoomOut() {
		zoomOutAround(this.getWidth() / 2, this.getHeight() / 2, 1 - zoomChangeFactor);
	}

	public void zoomOutAround(int centerX, int centerY, double zoomChangeFactor) {
		if (zoomFactor <= minimumZoomFactor) {
			zoomFactor = minimumZoomFactor;
		} else if (zoomFactor * zoomChangeFactor <= minimumZoomFactor) {
			renderPositionX = (int) (centerX - ((centerX - renderPositionX) * (minimumZoomFactor / zoomFactor)));
			renderPositionY = (int) (centerY - ((centerY - renderPositionY) * (minimumZoomFactor / zoomFactor)));
			
			zoomFactor = minimumZoomFactor;
		} else {
			renderPositionX = (int) (centerX - ((centerX - renderPositionX) * zoomChangeFactor));
			renderPositionY = (int) (centerY - ((centerY - renderPositionY) * zoomChangeFactor));
			
			zoomFactor *= zoomChangeFactor;
		}
		
		repaint();
	}
}