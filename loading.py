# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import streamlit as st
import time
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Generating...",
        page_icon="👋",
    )
    # st.markdown("<style>div.Widget.label-widget p {font-size: 48px;}</style>", unsafe_allow_html=True)
    progress_text = "Generating..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1, text=progress_text)
    st.success('Done!')
    st.balloons()

   

if __name__ == "__main__":
    run()
