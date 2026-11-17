def run_eval():
    print("开始执行 Eval 测试...")

    correct_trace = ["multiply", "add"]
    wrong_trace = ["add"]

    def assert_trace(trace):
        if "add" not in trace:
            return False, "违规：没有调用加法工具"
        if "multiply" not in trace:
            return False, "违规：跳过乘法直接算账"
        if trace.index("multiply") > trace.index("add"):
            return False, "违规：计算顺序错误，先加了运费再乘"

        return True, "通过"

    print("\n--- 测试正确轨迹 ---")
    passed, msg = assert_trace(correct_trace)
    if passed:
        print(f"✅ Trace 轨迹断言通过：{correct_trace}")
    else:
        print(f"❌ Trace 轨迹断言失败：{msg}")

    print("\n--- 测试错误轨迹 ---")
    passed, msg = assert_trace(wrong_trace)
    if not passed:
        print(f"✅ 成功拦截错误！原因：{msg}")
    else:
        print(f"❌ 漏报了！明明轨迹错了，但系统没发现。")


if __name__ == "__main__":
    run_eval()
