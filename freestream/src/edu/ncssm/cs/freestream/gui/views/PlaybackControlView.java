package edu.ncssm.cs.freestream.gui.views;

import javax.swing.JLabel;
import javax.swing.JSlider;
import javax.swing.JPanel;

@SuppressWarnings("serial")
public class PlaybackControlView extends JPanel {
	public PlaybackControlView() {
		this.add(new JLabel("PlaybackControlView"));
		this.add(new JSlider());
	}
}
