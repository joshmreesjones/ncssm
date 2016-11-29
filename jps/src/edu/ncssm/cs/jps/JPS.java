package edu.ncssm.cs.jps;

import edu.ncssm.cs.jps.controllers.JPSController;
import edu.ncssm.cs.jps.models.JPSModel;
import edu.ncssm.cs.jps.views.JPSView;

public class JPS {
	public static void main(String[] args) {
		JPSView view = new JPSView();
		JPSModel model = new JPSModel();
		
		@SuppressWarnings("unused")
		JPSController controller = new JPSController(view, model);
		
		view.setVisible(true);
	}
}