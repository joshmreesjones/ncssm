package edu.ncssm.cs.freestream.gui.views;

import java.awt.Dimension;

import javax.swing.JLabel;
import javax.swing.JPanel;

@SuppressWarnings("serial")
public class NavigationView extends JPanel {
	public NavigationView() {
		initView();
	}

	private void initView() {
		// height doesn't matter because the height will be set by the BorderLayout
		this.setPreferredSize(new Dimension(250, 0));
	}
}
