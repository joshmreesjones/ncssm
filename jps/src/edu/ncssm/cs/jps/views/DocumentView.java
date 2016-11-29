package edu.ncssm.cs.jps.views;

import java.awt.FlowLayout;
import java.awt.event.ActionListener;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;

import edu.ncssm.cs.jps.models.DocumentModel;

public class DocumentView {
	private CanvasPanelView canvasPanel;
	private JButton closeButton;
	private JPanel tabPanel;
	private JLabel tabLabel;
	
	public DocumentView(String title, ActionListener listener) {
		canvasPanel = new CanvasPanelView();
		
		FlowLayout flowLayout = new FlowLayout(FlowLayout.CENTER, 5, 0);
		tabPanel = new JPanel(flowLayout);
		tabPanel.setOpaque(false);
		tabLabel = new JLabel(title);
		
		closeButton = new JButton();
		closeButton.addActionListener(listener);
		closeButton.setOpaque(false);
		
		closeButton.setRolloverIcon(new ImageIcon(getClass().getResource("/res/closeTabButton.png")));
		closeButton.setRolloverEnabled(true);
		
		closeButton.setIcon(new ImageIcon(getClass().getResource("/res/closeTabButton_grayscale.png")));
		closeButton.setBorder(null);
		closeButton.setFocusable(false);
		
		tabPanel.add(tabLabel);
		tabPanel.add(closeButton);
		tabPanel.setBorder(BorderFactory.createEmptyBorder(2, 0, 0, 0));
	}
	
	public CanvasPanelView getCanvasPanelView() {
		return canvasPanel;
	}
	
	public JPanel getTabPanel() {
		return tabPanel;
	}
	
	public void setDocument(DocumentModel document) {
		canvasPanel.setDocument(document);
	}
}