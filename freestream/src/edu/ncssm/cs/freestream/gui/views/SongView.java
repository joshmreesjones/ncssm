package edu.ncssm.cs.freestream.gui.views;

import java.awt.Dimension;

import javax.swing.JLabel;
import javax.swing.JPanel;

@SuppressWarnings("serial")
public class SongView extends JPanel {
	public SongView() {
		this.setPreferredSize(new Dimension(250, 250));
		this.add(new JLabel("SongView"));
	}
}
