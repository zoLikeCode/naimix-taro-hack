import axios from 'axios';

export const GetTaroCards = async (card_name) => {
  try {
    const response = await axios.get(
      `http://go.itatmisis.ru:8000/get_taro_card/?card=${card_name}`,
    );
    return response.data;
  } catch (e) {
    console.error(e);
  }
};
