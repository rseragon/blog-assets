from manim import *

class DuffsCopy(Scene):
    def construct(self):
        code_str = """
int* duff(int* dst, const int* src, int len) {
    int n = (len + 3) / 4;

    switch(len % 4) {
        case 0: do { *dst++ = *src++;
        case 3: *dst++ = *src++;
        case 2: *dst++ = *src++;
        case 1: *dst++ = *src++;
            } while(--n);
    };

    return dst;
}
            """

        code = Code(code=code_str, language="c", insert_line_no=False, tab_width=2, font="Monospace", font_size=14)
        code.shift(RIGHT * 4)
        self.add(code)

        self.play(Indicate(code.code[1]), run_time=2)

        # Highlight the n = (len + 3) / 4 line
        self.play(Indicate(code.code[1]), run_time=2)


        self.wait(2)
