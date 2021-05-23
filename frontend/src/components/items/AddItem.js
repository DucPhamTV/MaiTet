// frontend/src/components/notes/AddNote.js
import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { Button, Form } from "react-bootstrap";
import { addItem } from "./ItemsActions";

class AddItem extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: "",
      description: "",
      price: 0
    };
  }
  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  onAddClick = () => {
    const item = {
      description: this.state.description,
      name: this.state.name,
      price: this.state.price,
    };
    this.props.addItem(item);
  };

  render() {
    return (
      <div>
        <h2>Add new Item</h2>
        <Form>
          <Form.Group controlId="contentId">
            <Form.Label>Item</Form.Label>
            <Form.Control
              as="textarea"
              rows={3}
              name="name"
              placeholder="Enter name"
              value={this.name}
              onChange={this.onChange}
            />
            <Form.Control
              as="textarea"
              rows={3}
              name="description"
              placeholder="Enter description"
              value={this.description}
              onChange={this.onChange}
            />
            <Form.Control
              as="textarea"
              rows={3}
              name="price"
              placeholder="Enter price"
              value={this.content}
              onChange={this.onChange}
            />
          </Form.Group>
        </Form>
        <Button variant="success" onClick={this.onAddClick}>
          Add Item
        </Button>
      </div>
    );
  }
}

AddItem.propTypes = {
  addItem: PropTypes.func.isRequired
};

const mapStateToProps = state => ({});

export default connect(mapStateToProps, { addItem })(withRouter(AddItem));
