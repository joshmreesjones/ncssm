package edu.ncssm.cs.jps.views;

import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.Cursor;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.awt.event.MouseWheelListener;
import java.io.File;
import java.math.RoundingMode;
import java.text.NumberFormat;
import java.util.ArrayList;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTabbedPane;
import javax.swing.JTextField;
import javax.swing.JToolBar;
import javax.swing.SwingUtilities;
import javax.swing.event.ChangeListener;
import javax.swing.filechooser.FileNameExtensionFilter;

import edu.ncssm.cs.jps.models.DocumentModel;

@SuppressWarnings("serial")
public class JPSView extends JFrame {
	private JMenuBar menuBar = new JMenuBar();
	
	private JMenu menuBar_file = new JMenu("File");
	private JMenu menuBar_view = new JMenu("View");
	
	private JMenuItem menuBar_file_open = new JMenuItem("Open");
	private JMenuItem menuBar_file_close = new JMenuItem("Close");
	private JMenuItem menuBar_file_exit = new JMenuItem("Exit");
	
	private JMenuItem menuBar_view_zoomIn = new JMenuItem("Zoom In");
	private JMenuItem menuBar_view_zoomOut = new JMenuItem("Zoom Out");
	private JMenuItem menuBar_view_zoomFit = new JMenuItem("Fit On Screen");
	private JMenuItem menuBar_view_zoomActualPixels = new JMenuItem("Zoom Actual Pixels");
	
	private JToolBar toolBar = new JToolBar(JToolBar.VERTICAL);
	private JButton toolBar_pan = new JButton();
	private JButton toolBar_zoom = new JButton();
	
	private JPanel mainPanel = new JPanel();
	
	private JTabbedPane documentsTabbedPane = new JTabbedPane();
	
	private JPanel statusBar = new JPanel();
	private JLabel statusBar_zoomLevelLabel = new JLabel("Zoom: ");
	private JTextField statusBar_zoomLevelTextField = new JTextField();
	NumberFormat percentFormatter;
	
	private ArrayList<DocumentView> documentViews = new ArrayList<DocumentView>();
	
	private ActionListener documentsTabbedPaneCloseButtonActionListener;
	private MouseListener canvasPanelViewMouseListener;
	private MouseMotionListener canvasPanelViewMouseMotionListener;
	private MouseWheelListener canvasPanelViewMouseWheelListener;

	private final String gifDescription = "CompuServe GIF (*.GIF)";
	private final String[] gifExtensions = {"gif"};
	private final FileNameExtensionFilter gifExtensionFilter = new FileNameExtensionFilter(gifDescription, gifExtensions);
	
	private final String pngDescription = "PNG (*.PNG)";
	private final String[] pngExtensions = {"png"};
	private final FileNameExtensionFilter pngExtensionFilter = new FileNameExtensionFilter(pngDescription, pngExtensions);
	
	private final String jpgDescription = "JPEG (*.JPG; *.JPEG; *.JPE)";
	private final String[] jpgExtensions = {"jpg", "jpeg", "jpe"};
	private final FileNameExtensionFilter jpgExtensionFilter = new FileNameExtensionFilter(jpgDescription, jpgExtensions);
	
	private final String bmpDescription = "BMP (*.BMP)";
	private final String[] bmpExtensions = {"bmp"};
	private final FileNameExtensionFilter bmpExtensionFilter = new FileNameExtensionFilter(bmpDescription, bmpExtensions);
	
	private final String wbmpDescription = "Wireless Bitmap";
	private final String[] wbmpExtensions = {"wbm", "wbmp"};
	private final FileNameExtensionFilter wbmpExtensionFilter = new FileNameExtensionFilter(wbmpDescription, wbmpExtensions);

	public JPSView() {
		this.percentFormatter = NumberFormat.getPercentInstance();
		this.percentFormatter.setMinimumIntegerDigits(1);
		this.percentFormatter.setMaximumIntegerDigits(4);
		this.percentFormatter.setMinimumFractionDigits(0);
		this.percentFormatter.setMaximumFractionDigits(3);
		
		this.percentFormatter.setRoundingMode(RoundingMode.HALF_UP);
		
		initGUI();
	}
	
	private void initGUI() {
		// Basic JFrame tasks
//		ImageIcon icon = new ImageIcon(getClass().getResource("/res/icon.png"));
//		this.setIconImage(icon.getImage());
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setMinimumSize(new Dimension(350, 300));
		this.setSize(800, 600);
		this.setTitle("JPS");
		this.setLocationRelativeTo(null);
		
		// Set menu items enabled or disabled
		menuBar_file_close.setEnabled(false);

		menuBar_view_zoomIn.setEnabled(false);
		menuBar_view_zoomOut.setEnabled(false);
		menuBar_view_zoomFit.setEnabled(false);
		menuBar_view_zoomActualPixels.setEnabled(false);
		
		statusBar.setEnabled(false);
		statusBar_zoomLevelLabel.setEnabled(false);
		statusBar_zoomLevelTextField.setEnabled(false);
		
		// Build GUI components
		menuBar.add(menuBar_file);
		menuBar.add(menuBar_view);
		
		menuBar_file.add(menuBar_file_open);
		menuBar_file.addSeparator();
		menuBar_file.add(menuBar_file_close);
		menuBar_file.addSeparator();
		menuBar_file.add(menuBar_file_exit);
		
		menuBar_view.add(menuBar_view_zoomIn);
		menuBar_view.add(menuBar_view_zoomOut);
		menuBar_view.add(menuBar_view_zoomFit);
		menuBar_view.add(menuBar_view_zoomActualPixels);
		
		toolBar_pan.setToolTipText("Pan Tool");
		toolBar_pan.setIcon(new ImageIcon(getClass().getResource("/res/panToolIcon.png")));
		toolBar_zoom.setToolTipText("Zoom Tool");
		toolBar_zoom.setIcon(new ImageIcon(getClass().getResource("/res/zoomToolIcon.png")));
		
		toolBar.add(toolBar_pan);
		toolBar.add(toolBar_zoom);
		
		statusBar.setLayout(new FlowLayout(FlowLayout.LEFT));
		statusBar.add(statusBar_zoomLevelLabel);
		statusBar_zoomLevelTextField.setColumns(6);
		statusBar.add(statusBar_zoomLevelTextField);
		
		mainPanel.setLayout(new BorderLayout());
		mainPanel.add(BorderLayout.CENTER, documentsTabbedPane);
		mainPanel.add(BorderLayout.SOUTH, statusBar);
		
		// Add mnemonics
		menuBar_file.setMnemonic(KeyEvent.VK_F);
		menuBar_view.setMnemonic(KeyEvent.VK_V);
		
		// Adjustments
		statusBar_zoomLevelTextField.setHorizontalAlignment(JTextField.CENTER);
		
		// Add final GUI components to frame
		this.setJMenuBar(menuBar);
		this.add(BorderLayout.WEST, toolBar);
		this.add(BorderLayout.CENTER, mainPanel);
	}
	
	public void addDocument(DocumentModel document) {
		menuBar_file_close.setEnabled(true);
		
		menuBar_view_zoomIn.setEnabled(true);
		menuBar_view_zoomOut.setEnabled(true);
		menuBar_view_zoomFit.setEnabled(true);
		menuBar_view_zoomActualPixels.setEnabled(true);
		
		statusBar.setEnabled(true);
		statusBar_zoomLevelLabel.setEnabled(true);
		statusBar_zoomLevelTextField.setEnabled(true);
		
		DocumentView newDocumentView = new DocumentView(document.getTitle(), documentsTabbedPaneCloseButtonActionListener);
		
		documentViews.add(newDocumentView);
		newDocumentView.setDocument(document);
		
		CanvasPanelView newCanvasPanelView = newDocumentView.getCanvasPanelView();
		documentsTabbedPane.add(newCanvasPanelView);
		
		newCanvasPanelView.addMouseListener(canvasPanelViewMouseListener);
		newCanvasPanelView.addMouseMotionListener(canvasPanelViewMouseMotionListener);
		newCanvasPanelView.addMouseWheelListener(canvasPanelViewMouseWheelListener);
		
		int newDocumentIndex = documentsTabbedPane.indexOfComponent(newCanvasPanelView);

		documentsTabbedPane.setTabComponentAt(newDocumentIndex, newDocumentView.getTabPanel());
		documentsTabbedPane.setSelectedIndex(newDocumentIndex);
		
		SwingUtilities.invokeLater(new Runnable() {
			@Override
			public void run() {
				setZoomFit();
			}
		});
	}
	
	public void removeDocument(int index) {
		documentViews.remove(index);
		documentsTabbedPane.remove(index);
		
		if (documentsTabbedPane.getTabCount() == 0) {
			menuBar_file_close.setEnabled(false);
			
			menuBar_view_zoomIn.setEnabled(false);
			menuBar_view_zoomOut.setEnabled(false);
			menuBar_view_zoomFit.setEnabled(false);
			menuBar_view_zoomActualPixels.setEnabled(false);

			statusBar.setEnabled(false);
			statusBar_zoomLevelLabel.setEnabled(false);
			statusBar_zoomLevelTextField.setEnabled(false);
			
			statusBar_zoomLevelTextField.setText("");
		}
	}
	
	public File showAndGetValueOfFileChooser() {
		JFileChooser fileChooser = new JFileChooser();
		
		fileChooser.addChoosableFileFilter(gifExtensionFilter);
		fileChooser.addChoosableFileFilter(pngExtensionFilter);
		fileChooser.addChoosableFileFilter(jpgExtensionFilter);
		fileChooser.addChoosableFileFilter(bmpExtensionFilter);
		fileChooser.addChoosableFileFilter(wbmpExtensionFilter);
		
		int returnState = fileChooser.showOpenDialog(this);
		
		if (returnState == JFileChooser.APPROVE_OPTION) {
			return fileChooser.getSelectedFile();
		}
		
		return null;
	}
	
	public void showMessageDialog(String message, String title, int type) {
		JOptionPane.showMessageDialog(this, message, title, type);
	}
	
	public void repaintCanvasPanelView() {
		getCurrentCanvasPanelView().repaint();
	}
	
	private CanvasPanelView getCurrentCanvasPanelView() {
		try {
			return (CanvasPanelView) documentsTabbedPane.getComponentAt(getSelectedTab());
		} catch(IndexOutOfBoundsException exception) {
			return null;
		}
	}
	
	public double getFrameHeight() {
		return this.getBounds().getHeight();
	}
	
	public double getFrameWidth() {
		return this.getBounds().getWidth();
	}
	
	public int getIndexOfTabComponent(Container container) {
		return documentsTabbedPane.indexOfTabComponent(container);
	}
	
	public int getRenderPositionX() {
		return getCurrentCanvasPanelView().getRenderPositionX();
	}
	
	public int getRenderPositionY() {
		return getCurrentCanvasPanelView().getRenderPositionY();
	}
	
	public int getSelectedTab() {
		return documentsTabbedPane.getSelectedIndex();
	}
	
	public int getTabCount() {
		return documentsTabbedPane.getTabCount();
	}
	
	public double getZoomFactor() {
		return getCurrentCanvasPanelView().getZoomFactor();
	}
	
	public void setCurrentCursor(Cursor cursor) {
		CanvasPanelView currentPanel = getCurrentCanvasPanelView();
		
		if (currentPanel != null) {
			currentPanel.setCursor(cursor);
		}
	}
	
	public void setRenderPositionX(int renderPositionX) {
		getCurrentCanvasPanelView().setRenderPositionX(renderPositionX);
	}
	
	public void setRenderPositionY(int renderPositionY) {
		getCurrentCanvasPanelView().setRenderPositionY(renderPositionY);
	}
	
	public void setStatusBar_zoomLevelTextField(double zoomFactor) {
		statusBar_zoomLevelTextField.setText(percentFormatter.format(zoomFactor));
	}
	
	public void setZoomActualPixels() {
		getCurrentCanvasPanelView().setZoomActualPixels();
		updateZoomFactor();
	}
	
	public void setZoomFactor(double zoomFactor) {
		getCurrentCanvasPanelView().setZoomFactor(zoomFactor);
	}
	
	public void setZoomFactorAround(int centerX, int centerY, double zoomFactor) {
		getCurrentCanvasPanelView().setZoomFactorAround(centerX, centerY, zoomFactor);
	}
	
	public void setZoomFit() {
		getCurrentCanvasPanelView().setZoomFit();
		updateZoomFactor();
	}
	
	public void zoomIn() {
		getCurrentCanvasPanelView().zoomIn();
		updateZoomFactor();
	}
	
	public void zoomInAround(int centerX, int centerY) {
		zoomInAround(centerX, centerY, getCurrentCanvasPanelView().getZoomChangeFactor());
		updateZoomFactor();
	}
	
	public void zoomInAround(int centerX, int centerY, double zoomChangeFactor) {
		getCurrentCanvasPanelView().zoomInAround(centerX, centerY, 1 + zoomChangeFactor);
		updateZoomFactor();
	}
	
	public void zoomOut() {
		getCurrentCanvasPanelView().zoomOut();
		updateZoomFactor();
	}
	
	public void zoomOutAround(int centerX, int centerY) {
		zoomOutAround(centerX, centerY, getCurrentCanvasPanelView().getZoomChangeFactor());
		updateZoomFactor();
	}
	
	public void zoomOutAround(int centerX, int centerY, double zoomChangeFactor) {
		getCurrentCanvasPanelView().zoomOutAround(centerX, centerY, 1 - zoomChangeFactor);
		updateZoomFactor();
	}
	
	public void updateZoomFactor() {
		updateStatusBar_zoomLevelTextField();
		
		CanvasPanelView currentPanel = getCurrentCanvasPanelView();
		if (currentPanel.getZoomFactor() >= currentPanel.getMaximumZoomFactor()) {
			menuBar_view_zoomIn.setEnabled(false);
		} else if (currentPanel.getZoomFactor() <= currentPanel.getMinimumZoomFactor()) {
			menuBar_view_zoomOut.setEnabled(false);
		} else {
			menuBar_view_zoomIn.setEnabled(true);
			menuBar_view_zoomOut.setEnabled(true);
		}
	}
	
	public void updateStatusBar_zoomLevelTextField() {
		setStatusBar_zoomLevelTextField(getCurrentCanvasPanelView().getZoomFactor());
	}
	
	public void addMenuBarFileOpenActionListener(ActionListener listener) {
		menuBar_file_open.addActionListener(listener);
	}
	
	public void addMenuBarFileCloseActionListener(ActionListener listener) {
		menuBar_file_close.addActionListener(listener);
	}
	
	public void addMenuBarFileExitActionListener(ActionListener listener) {
		menuBar_file_exit.addActionListener(listener);
	}
	
	public void addMenuBarViewZoomInActionListener(ActionListener listener) {
		menuBar_view_zoomIn.addActionListener(listener);
	}
	
	public void addMenuBarViewZoomOutActionListener(ActionListener listener) {
		menuBar_view_zoomOut.addActionListener(listener);
	}
	
	public void addMenuBarViewZoomFitActionListener(ActionListener listener) {
		menuBar_view_zoomFit.addActionListener(listener);
	}
	
	public void addMenuBarViewZoomActualPixelsActionListener(ActionListener listener) {
		menuBar_view_zoomActualPixels.addActionListener(listener);
	}
	
	public void setCanvasPanelViewMouseListener(MouseListener listener) {
		canvasPanelViewMouseListener = listener;
	}
	
	public void setCanvasPanelViewMouseMotionListener(MouseMotionListener listener) {
		canvasPanelViewMouseMotionListener = listener;
	}

	public void setCanvasPanelViewMouseWheelListener(MouseWheelListener listener) {
		canvasPanelViewMouseWheelListener = listener;
	}
	
	public void addStatusBar_zoomLevelTextFieldActionListener(ActionListener listener) {
		statusBar_zoomLevelTextField.addActionListener(listener);
	}
	
	public void addDocumentsTabbedPaneChangeListener(ChangeListener listener) {
		documentsTabbedPane.addChangeListener(listener);
	}
	
	public void setDocumentsTabbedPaneCloseButtonActionListener(ActionListener listener) {
		this.documentsTabbedPaneCloseButtonActionListener = listener;
	}
	
	public void addToolBarPanToolActionListener(ActionListener listener) {
		toolBar_pan.addActionListener(listener);
	}
	
	public void addToolBarZoomToolActionListener(ActionListener listener) {
		toolBar_zoom.addActionListener(listener);
	}
}