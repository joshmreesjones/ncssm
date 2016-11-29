package edu.ncssm.cs.freestream;

import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * An implementation of a queue to hold songs.
 * 
 * This PlayQueue has a very similar implementation to LinkedList.
 * This implementation does not allow null values to be added
 * because it will be used to queue songs in FreeStream and
 * we will not be queueing null songs.
 * 
 * element() was not implemented because peek() will suit the needs
 * of FreeStream.
 * 
 * offer(E e) was not implemented because there is no size restriction
 * on the PlayQueue.
 * 
 * remove() was not implemented because poll() will suit the needs
 * of FreeStream.
 * 
 * @author Josh Rees-Jones
 * @author Mitch Rees-Jones
 */
public class PlayQueue<E> implements Iterable<E> {
	/**
	 * A container for each element of the queue.
	 * 
	 * A Node holds a data object and a reference to the next and
	 * last nodes.
	 */
	private class Node<E> {
		// the data held by the Node
		private E data;

		// references to the next and last nodes
		private Node<E> next;
		private Node<E> previous;

		/**
		 * Constructs a new Node of type E with the specified data
		 * and references.
		 * 
		 * @param data the data to be held by this Node
		 * @param previous the reference to the previous Node
		 * @param next the reference to the next Node
		 */
		public Node(E data, Node<E> previous, Node<E> next) {
			this.data = data;

			this.previous = previous;
			this.next = next;
		}

		/**
		 * Returns this Node's data.
		 * 
		 * @return this Node's data
		 */
		public E getData() {
			return data;
		}

		/**
		 * Returns a reference to the previous node.
		 * 
		 * @return a reference to the previous node
		 */
		public Node<E> getPrevious() {
			return previous;
		}

		/**
		 * Returns a reference to the next node.
		 * 
		 * @return a reference to the next node
		 */
		public Node<E> getNext() {
			return next;
		}

		/**
		 * Sets the data of this Node.
		 * 
		 * @param data the data to be set for this Node
		 * @throws IllegalArgumentException if data is null
		 */
		public void setData(E data) {
			if (data == null) {
				throw new IllegalArgumentException();
			}

			this.data = data;
		}

		/**
		 * Sets the reference to the previous Node.
		 * 
		 * @param previous the reference to be set to the previous Node
		 */
		public void setPrevious(Node<E> previous) {
			this.previous = previous;
		}

		/**
		 * Sets the reference to the next Node.
		 * 
		 * @param next the reference to be set to the next Node
		 */
		public void setNext(Node<E> next) {
			this.next = next;
		}
	}

	// the front of this PlayQueue (this item is ready for dequeueing)
	private Node<E> front;

	// the back of this PlayQueue (this is the most recently queued item)
	private Node<E> back;

	/**
	 * Inserts the specified element into the back of the queue.
	 * 
	 * @param e the element to be added
	 * @return true if the the element was successfully added
	 */
	public boolean add(E e) {
		if (front == null) {
			// queue is empty
			front = back = new Node<E>(e, null, null);
		} else {
			// put a new Node on the back
			Node<E> newNode = new Node<E>(e, back, null);

			back.setNext(newNode);
			back = newNode;
		}

		return true;
	}

	/**
	 * Adds all of the elements in the specified collection to the back of
	 * this PlayQueue. addAll() treats the collection like its first element
	 * should be the first element queued.
	 * 
	 * @param collection the collection to be added to this PlayQueue
	 * @return true if the collection has been changed as a result of this method call
	 */
	public boolean addAll(Iterable<? extends E> iterable) {
		boolean changed = false;

		if (iterable == null) {
			throw new NullPointerException();
		} else {
			for (E element : iterable) {
				if (element == null) {
					throw new NullPointerException();
				} else {
					add(element);
					changed = true;
				}
			}
		}

		return changed;
	}

	/**
	 * Returns an iterator over the queue.
	 * 
	 * @return an iterator over the queue
	 */
	public Iterator<E> iterator() {
		return new PlayQueueIterator<E>();
	}

	/**
	 * The Iterator object returned by PlayQueue.iterator().
	 * 
	 * This iterator beings iteration at the front of the queue and
	 * iterates to the back. The first call of next() returns the
	 * front of the queue and the last call of next() returns the
	 * back of the queue.
	 */
	private class PlayQueueIterator<E> implements Iterator<E> {
		private PlayQueue.Node currentNode;

		public PlayQueueIterator() {
			currentNode = PlayQueue.this.front;
		}

		/**
		 * Returns true if this iteration has more elements.
		 * 
		 * @return true if this iteration has more elements
		 */
		public boolean hasNext() {
			return !(currentNode == null);
		}

		/**
		 * Returns the next element in this iteration.
		 * 
		 * @return the next element in this iteration
		 */
		public E next() {
			if (currentNode == null) {
				throw new NoSuchElementException();
			}

			@SuppressWarnings("unchecked")
			E data = (E) currentNode.getData();
			currentNode = currentNode.getNext();
			return data;
		}

		/**
		 * Removes the last element of the underlying collection returned
		 * from next(). This operation is unsupported for our PlayQueue.
		 */
		public void remove() {
			throw new UnsupportedOperationException();
		}
	}

	/**
	 * Retrieves the front of this PlayQueue, but does not remove it.
	 * 
	 * @return the front of this PlayQueue, or null if this PlayQueue is empty
	 */
	public E peek() {
		return front == null ? null : front.getData();
	}

	/**
	 * Retrieves and removes the front of this PlayQueue.
	 * 
	 * @return the front of this PlayQueue, or null if thus PlayQueue is empty
	 */
	public E poll() {
		if (front == null) {
			// the queue is empty
			return null;
		} else if (front == back) {
			// the queue has one item in it
			Node<E> oldFront = front;

			front = null;
			back = null;

			return oldFront.getData();
		} else {
			Node<E> oldFront = front;

			// reset front
			front = front.getNext();
			front.setPrevious(null);

			return oldFront.getData();
		}
	}

	/**
	 * Returns a string representation of this PlayQueue.
	 * 
	 * The PlayQueue is represented as a series of comma-separated values
	 * enclosed by brackets. The first element displayed is the front of the
	 * PlayQueue, and the last element displayed is the back of the PlayQueue.
	 * 
	 * @return the string representation of this PlayQueue
	 */
	public String toString() {
		if (back == null) {
			return "[]";
		}

		String result = "[";
		Node<E> node = front;

		while (node.getNext() != null) {
			result += node.getData().toString() + ",";
			node = node.getNext();
		}

		return result + node.getData().toString() + "]";
	}
}
