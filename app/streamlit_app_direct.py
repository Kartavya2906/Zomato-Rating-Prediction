import streamlit as st
import joblib
import json
import numpy as np
import os
st.title("🍽️ Restaurant Rating Predictor")
# =========================
# Load model & metadata
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__)).rstrip("/app")

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "zomato_rating_model_rmse_0.321_20251229_0230.joblib"
)

META_PATH = os.path.join(
    BASE_DIR,
    "model",
    "zomato_rating_model_metadata_20251229_0230.json"
)
#   #
@st.cache_resource
def load_artifacts():
    model = joblib.load(MODEL_PATH)
    with open(META_PATH, "r") as f:
        meta = json.load(f)
    return model, meta

model, meta = load_artifacts()
feature_order = meta["features"]
# -------- Binary inputs ----------
online_order = st.radio("Online Order Available?", ["Yes", "No"])
book_table = st.radio("Table Booking Available?", ["Yes", "No"])

# -------- Numerical inputs ----------
votes = st.number_input("Number of Votes", min_value=0, step=10)
approx_cost = st.number_input("Approx Cost for Two", min_value=50, step=50)

# -------- Dropdowns ----------
rest_type = st.selectbox(
    "Restaurant Type",
   ['Bakery', 'Bar', 'Beverage Shop', 'Bhojanalya', 'Cafe',
       'Casual Dining', 'Club', 'Confectionery', 'Delivery',
       'Dessert Parlor', 'Dhaba', 'Fine Dining', 'Food Court',
       'Food Truck', 'Kiosk', 'Lounge', 'Mess', 'Microbrewery', 'Pub',
       'Quick Bites', 'Sweet Shop', 'Takeaway', 'Unknown']
)

location = st.selectbox(
    "Location",
    ['Jayanagar', 'JP Nagar', 'BTM', 'Marathahalli',
       'Koramangala 5th Block', 'HSR', 'Whitefield', 'Indiranagar','Other']
)

listed_city = st.selectbox(
    "Listed In (City)",
    ['BTM', 'Church Street', 'Indiranagar', 'Jayanagar',
       'JP Nagar', 'Koramangala 4th Block', 'Koramangala 5th Block',
       'Koramangala 6th Block', 'Koramangala 7th Block', 'MG Road','Other']
)

listed_type = st.selectbox(
    "Listed In (Type)",
   ['Buffet', 'Cafes', 'Delivery', 'Desserts', 'Dine-out',
       'Drinks & nightlife', 'Pubs and bars']
)

# -------- Multi-select cuisines ----------
cuisines = st.multiselect(
    "Cuisines",
   ['North Indian', ' Mughlai', ' Chinese', 'Chinese', ' North Indian',
       ' Thai', 'Cafe', ' Mexican', ' Italian', 'South Indian',
       ' Rajasthani', ' South Indian', ' Andhra', 'Pizza', ' Cafe',
       ' Continental', ' Momos', ' Beverages', ' Fast Food', ' American',
       ' French', ' Pizza', 'Italian', ' European', ' Bakery', ' Burger',
       'Bakery', ' Desserts', ' Biryani', 'Biryani', 'Street Food',
       'Burger', ' Rolls', 'Fast Food', ' Street Food', 'Ice Cream',
       'Healthy Food', ' Salad', 'Asian', ' Korean', ' Indonesian',
       ' Japanese', 'Desserts', 'Goan', ' Seafood', ' Kebab',
       'Continental', ' Steak', 'Seafood', 'Beverages', ' Ice Cream',
       'Mithai', ' Iranian', ' Sandwich', 'Sandwich', ' Juices',
       ' Mithai', 'Thai', ' Vietnamese', ' Asian', 'Salad',
       ' Healthy Food', ' Hyderabadi', 'Bengali', 'Arabian',
       'Mangalorean', ' BBQ', 'Vietnamese', 'Andhra', ' Arabian',
       ' Mangalorean', ' Tea', 'Juices', ' Afghani', 'Mexican', 'Rolls',
       ' Lebanese', ' Finger Food', 'Tibetan', 'Tea', 'Momos', ' Tibetan',
       'Unknown', ' Charcoal Chicken', 'Hyderabadi', 'Finger Food',
       'Mughlai', ' Middle Eastern', ' Mediterranean', 'BBQ', ' Wraps',
       'Kerala', ' Kerala', 'Oriya', ' Bihari', ' Roast Chicken',
       'Maharashtrian', 'Bohri', 'Kebab', 'African', 'American',
       ' Bengali', 'Rajasthani', ' Nepalese', 'Turkish', 'Tamil',
       ' Tex-Mex', ' Belgian', ' Gujarati', 'Roast Chicken', 'Gujarati',
       'South American', ' Oriya', 'Konkan', 'European', ' Chettinad',
       ' Coffee', ' Turkish', ' Indian', ' Maharashtrian', ' Afghan',
       ' Modern Indian', ' Goan', ' Lucknowi', 'Japanese',
       'Modern Indian', 'Bihari', 'Lebanese', 'Australian',
       'Mediterranean', 'Steak', 'Spanish', ' Malaysian', ' Burmese',
       ' Sushi', 'Portuguese', ' African', 'Parsi', 'Nepalese', ' Greek',
       'North Eastern', 'Chettinad', ' Bar Food', ' Konkan', ' Spanish',
       ' Singaporean', 'Awadhi', ' Naga', 'Lucknowi', ' Kashmiri',
       'Korean', ' Cantonese', 'Malaysian', ' Grill', 'Sushi',
       ' Bubble Tea', ' Hot dogs', 'Kashmiri', 'French', ' Assamese',
       ' Awadhi', 'Assamese', 'Coffee', ' Sri Lankan', ' Mongolian',
       ' Paan', ' Parsi', 'Charcoal Chicken', ' North Eastern',
       'Bar Food', ' British', 'Singaporean', 'Middle Eastern', 'Naga',
       ' Pan Asian', 'Belgian', ' German', 'Indonesian', 'Burmese',
       'Russian', ' Drinks Only', ' Jewish', ' Vegan', 'Iranian',
       ' Raw Meats', 'German', ' Sindhi', 'British']
)
top_cuisines=['North Indian', 'North Indian, Chinese', 'South Indian',
       'Bakery, Desserts', 'Cafe', 'Biryani', 'Desserts',
       'South Indian, North Indian, Chinese', 'Fast Food', 'Bakery', 'Chinese',
       'Ice Cream, Desserts', 'Chinese, North Indian', 'Mithai, Street Food',
       'North Indian, Chinese, Biryani', 'Desserts, Ice Cream',
       'Desserts, Beverages', 'Finger Food', 'North Indian, South Indian',
       'South Indian, North Indian', 'Beverages, Fast Food',
       'North Indian, Biryani', 'Chinese, Momos',
       'North Indian, South Indian, Chinese', 'Beverages']
# -------- Feature Engineering ----------
data = {
    "online_order": 1 if online_order == "Yes" else 0,
    "book_table": 1 if book_table == "Yes" else 0,
    "votes": votes,
    "approx_cost": approx_cost,
    "cuisines_count": len(cuisines),
    "pop_cuisines_count": len(set(cuisines) & set(top_cuisines)),
    f"rest_type_first_{rest_type}": 1,
    f"location_{location}": 1,
    f"listed_in(city)_{listed_city}": 1,
    f"listed_in(type)_{listed_type}": 1
}

# -------- Prediction ----------
if st.button("Predict Rating"):
    try:
        # Ensure all features are present in correct order
        input_vector = np.array([
            data.get(feature, 0) for feature in feature_order
        ]).reshape(1, -1)

        prediction = model.predict(input_vector)[0]

        st.success(f"⭐ Predicted Rating: {round(float(prediction), 2)}")

    except Exception as e:
        st.error("Prediction failed.")
        st.exception(e)

