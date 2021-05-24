import { GET_ITEMS, ADD_ITEM, DELETE_ITEM, UPDATE_ITEM } from "./ItemsTypes";

const initialState = {
    items: []
};

export const itemsReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_ITEMS:
            return {
                ...state,
                items: action.payload,
            };
        case ADD_ITEM:
            return {
                ...state,
                items: [...state.items, action.payload],
            };
        case DELETE_ITEM:
            return {
                ...state,
                items: state.items.filter((item, index) => item.uuid !== action.payload),
            };
        case UPDATE_ITEM:
            const updatedItems = state.items.map(item => {
                if (item.uuid === action.payload.id) {
                    return { ...item, ...action.payload };
                }
                return item;
            });
            return {
                ...state,
                items: updatedItems,
            };
        default:
            return state;
    }
};
