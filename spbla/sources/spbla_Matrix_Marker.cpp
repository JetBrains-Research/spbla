/**********************************************************************************/
/* MIT License                                                                    */
/*                                                                                */
/* Copyright (c) 2020, 2021 JetBrains-Research                                    */
/*                                                                                */
/* Permission is hereby granted, free of charge, to any person obtaining a copy   */
/* of this software and associated documentation files (the "Software"), to deal  */
/* in the Software without restriction, including without limitation the rights   */
/* to use, copy, modify, merge, publish, distribute, sublicense, and/or sell      */
/* copies of the Software, and to permit persons to whom the Software is          */
/* furnished to do so, subject to the following conditions:                       */
/*                                                                                */
/* The above copyright notice and this permission notice shall be included in all */
/* copies or substantial portions of the Software.                                */
/*                                                                                */
/* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR     */
/* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,       */
/* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE    */
/* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER         */
/* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  */
/* OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  */
/* SOFTWARE.                                                                      */
/**********************************************************************************/

#include <spbla_Common.hpp>
#include <cstring>
#include <cmath>

spbla_Status spbla_Matrix_Marker(
        spbla_Matrix matrix,
        char* marker,
        spbla_Index* size
) {
    SPBLA_BEGIN_BODY
        SPBLA_VALIDATE_LIBRARY
        SPBLA_ARG_NOT_NULL(matrix)
        SPBLA_ARG_NOT_NULL(size)

        auto m = (spbla::Matrix*) matrix;
        auto actualSize = m->getDebugMarkerSizeWithNullT();
        auto toCopy = std::min(*size, actualSize);

        if (marker != nullptr && toCopy > 0) {
            // C str (with \0)
            const auto* text = m->getDebugMarker();
            std::memcpy(marker, text, toCopy);

            // Explicitly terminate (for case size < actualSize)
            marker[toCopy - 1] = '\0';
        }

        *size = actualSize;
    SPBLA_END_BODY
}