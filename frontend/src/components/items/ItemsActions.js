import axios from "axios";
import { toastOnError } from "../../utils/Utils";
import { GET_ITEMS, ADD_ITEM } from "./ItemsTypes";

export const getItems = () => dispatch => {
    axios
        .get("/v1/items/")
        .then(response => {
            dispatch({
                type: GET_ITEMS,
                payload: response.data,
            });
        })
        .catch(error => {
            toastOnError(error);
        });
};

export const addItem = item => dispatch => {
    axios
        .post("v1/items/", item)
        .then(response => {
            dispatch({
                type: ADD_ITEM,
                payload: response.data,
            });
        })
        .catch(error => {
            toastOnError(error);
        });
};