package edu.ncssm.cs.jps.controllers;

import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.awt.event.MouseWheelEvent;
import java.awt.event.MouseWheelListener;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.JButton;
import javax.swing.JOptionPane;
import javax.swing.JTabbedPane;
import javax.swing.JTextField;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.event.MouseInputAdapter;

import edu.ncssm.cs.jps.controllers.tools.PanTool;
import edu.ncssm.cs.jps.controllers.tools.ZoomTool;
import edu.ncssm.cs.jps.models.DocumentModel;
import edu.ncssm.cs.jps.models.JPSModel;
import edu.ncssm.cs.jps.views.JPSView;

public class JPSController {
	JPSModel model;
	JPSView view;
	
	PanTool panTool;
	ZoomTool zoomTool;
	
	Toolkit toolkit;
	
	public JPSController(JPSView view, JPSModel model) {
		this.model = model;
		this.view = view;
		
		toolkit = Toolkit.getDefaultToolkit();
		
		panTool = new PanTool(view);
		zoomTool = new ZoomTool(view);
		
		model.setCurrentTool(panTool);
		
		this.view.addMenuBarFileOpenActionListener(new MenuBarFileOpenActionListener());
		this.view.addMenuBarFileCloseActionListener(new MenuBarFileCloseActionListener());
		this.view.addMenuBarFileExitActionListener(new MenuBarFileExitActionListener());
		
		this.view.addMenuBarViewZoomInActionListener(new MenuBarViewZoomInActionListener());
		this.view.addMenuBarViewZoomOutActionListener(new MenuBarViewZoomOutActionListener());
		this.view.addMenuBarViewZoomFitActionListener(new MenuBarViewZoomFitActionListener());
		this.view.addMenuBarViewZoomActualPixelsActionListener(new MenuBarViewZoomActualPixelsActionListener());
		
		this.view.setCanvasPanelViewMouseListener(new CanvasPanelViewMouseListener());
		this.view.setCanvasPanelViewMouseMotionListener(new CanvasPanelViewMouseMotionListener());
		this.view.setCanvasPanelViewMouseWheelListener(new CanvasPanelViewMouseWheelListener());
		
		this.view.addStatusBar_zoomLevelTextFieldActionListener(new StatusBar_zoomLevelTextFieldActionListener());
		
		this.view.addDocumentsTabbedPaneChangeListener(new DocumentsTabbedPaneChangeListener());
		this.view.setDocumentsTabbedPaneCloseButtonActionListener(new DocumentsTabbedPaneCloseButtonActionListener());
		
		this.view.addToolBarPanToolActionListener(new ToolBarPanToolActionListener());
		this.view.addToolBarZoomToolActionListener(new ToolBarZoomToolActionListener());
	}
	
	private class MenuBarFileOpenActionListener implements ActionListener {
		@Override
		public void actionPerformed(ActionEvent event) {
			File fileChooserReturnValue = view.showAndGetValueOfFileChooser();
			
			if (fileChooserReturnValue != null) {
				try {
					DocumentModel newDocument = new DocumentModel(ImageIO.read(fileChooserReturnValue), fileChooserReturnValue.getAbsolutePath(), fileChooserReturnValue.getName());
					model.addDocument(newDocument);
					view.addDocument(newDocument);
				} catch(IOException exception) {
				} catch(Exception exception) {
					view.showMessageDialog("An error occurred opening the image. Please\n" +
										   "open images of type .png, .jpg, .bmp, or .wbmp.",
										   "Error Opening Image", JOptionPane.ERROR_MESSAGE);
				}
			}
			
			view.setCurrentCursor(model.getCurrentTool().getCursor());
		}
	}
	
	private class MenuBarFileCloseActionListener implements ActionListener {
		@Override
		public void actionPerformed(ActionEvent event) {
			if (view.getTabCount() > 0) {
				view.removeDocument(view.getSelectedTab());
			}
		}
	}
	
	private class MenuBarFileExitActionListener implements ActionListener {
		@Override
		public void actionPerformed(ActionEvent event) {
			view.setVisible(false);
			
			System.exit(0);
		}
	}
	
	private class MenuBarViewZoomInActionListener implements ActionListener {
		@Override
		public void actionPerformed(ActionEvent event) {
			view.zoomIn();
		}
	}
	
	private class MenuBarViewZoomOutActionListener implements ActionListener {
		@Override
		public void actionPerformed(ActionEvent event) {
			view.zoomOut();
		}
	}
	
	private class MenuBarViewZoomFitActionListener implements ActionListener {
		@Override
		public void actionPerformed(ActionEvent event) {
			view.setZoomFit();
		}
	}
	
	private class MenuBarViewZoomActualPixelsActionListener implements ActionListener {
		@Override
		public void actionPerformed(ActionEvent event) {
			view.setZoomActualPixels();
		}
	}
	
	private class CanvasPanelViewMouseListener extends MouseInputAdapter implements MouseListener {
		@Override
		public void mouseClicked(MouseEvent event) {
			JPSController.this.model.getCurrentTool().mouseClicked(event);
		}

		@Override
		public void mouseEntered(MouseEvent event) {
			JPSController.this.model.getCurrentTool().mouseEntered(event);
		}

		@Override
		public void mouseExited(MouseEvent event) {
			JPSController.this.model.getCurrentTool().mouseExited(event);
		}

		@Override
		public void mousePressed(MouseEvent event) {
			JPSController.this.model.getCurrentTool().mousePressed(event);
		}

		@Override
		public void mouseReleased(MouseEvent event) {
			JPSController.this.model.getCurrentTool().mouseReleased(event);
		}
	}
	
	private class CanvasPanelViewMouseMotionListener implements MouseMotionListener {
		@Override
		public void mouseDragged(MouseEvent event) {
			JPSController.this.model.getCurrentTool().mouseDragged(event);
		}

		@Override
		public void mouseMoved(MouseEvent event) {
			JPSController.this.model.getCurrentTool().mouseMoved(event);
		}
	}
	
	private class CanvasPanelViewMouseWheelListener implements MouseWheelListener {
		@Override
		public void mouseWheelMoved(MouseWheelEvent event) {
			JPSController.this.model.getCurrentTool().mouseWheelMoved(event);
		}
	}
	
	private class StatusBar_zoomLevelTextFieldActionListener implements ActionListener {
		@Override
		public void actionPerformed(ActionEvent event) {
			String zoomLevelValue = ((JTextField) event.getSource()).getText();
			int length = zoomLevelValue.length();
			
			if (zoomLevelValue.substring(length - 1, length).equals("%")) {
				zoomLevelValue = zoomLevelValue.substring(0, length - 1);
			}
			
			try {
				double zoomFactor = Double.parseDouble(zoomLevelValue) / 100;
				
				view.setZoomFactorAround(view.getWidth() / 2, view.getHeight() / 2, zoomFactor);
				view.updateZoomFactor();
			} catch(NumberFormatException exception) {
				toolkit.beep();
				view.showMessageDialog("Invalid numeric entry. A number between 12.50%\n" +
									   "and 3200.00% is required. Previous value inserted.",
									   "Invalid Entry",
									   JOptionPane.ERROR_MESSAGE);
				
				view.updateZoomFactor();
			}
		}
	}
	
	private class DocumentsTabbedPaneChangeListener implements ChangeListener {
		@Override
		public void stateChanged(ChangeEvent event) {
			if (((JTabbedPane) event.getSource()).getTabCount() != 0) {
				view.updateZoomFactor();
			}
		}
	}
	
	private class DocumentsTabbedPaneCloseButtonActionListener implements ActionListener {
		@Override
		public void actionPerformed(ActionEvent event) {
			view.removeDocument(view.getIndexOfTabComponent(((JButton) event.getSource()).getParent()));
		}
	}
	
	private class ToolBarPanToolActionListener implements ActionListener {
		@Override
		public void actionPerformed(ActionEvent event) {
			model.setCurrentTool(panTool);
			view.setCurrentCursor(panTool.getCursor());
		}
	}
	
	private class ToolBarZoomToolActionListener implements ActionListener {
		@Override
		public void actionPerformed(ActionEvent event) {
			model.setCurrentTool(zoomTool);
			view.setCurrentCursor(zoomTool.getCursor());
		}
	}
}