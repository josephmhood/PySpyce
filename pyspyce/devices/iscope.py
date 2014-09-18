"""Current Scope Device."""

import pyspyce.interfaces as inter
import pyspyce.sandbox as sb


class IScope(inter.MNADevice, inter.CurrentSensor):

    def __init__(self, nodes, **parameters):
        inter.MNADevice.__init__(self, nodes, 1, **parameters)
        self.time = []
        self.data = []

    def connect(self):
        nplus, nminus = self.nodes
        self.port2node = {0: self.get_node_index(nplus),
                          1: self.get_node_index(nminus),
                          2: self.create_internal("{0}_int".format(self.name))}

    def start(self, dt):
        self.jac[0, 2] = 1.0
        self.jac[1, 2] = -1.0
        self.jac[2, 0] = 1.0
        self.jac[2, 1] = -1.0

    def step(self, dt, t):
        pass

    def post_step(self, dt, t):
        i = self.get_across(2)
        self.time.append(t)
        self.data.append(i)

    def get_current_node(self):
        return self.port2node[2], -1.0


class IScopeBlock(sb.Block):
    """Schematic graphical inteface for IScope device."""
    friendly_name = "Current Scope"
    family = "Meters"
    label = "Scope"
    engine = IScope

    def __init__(self, name):
        # init super:
        sb.Block.__init__(self, name, None)
        self.size = (160, 120)
        self.margin = 12

        # port:
        self.ports['positive'] = sb.Port(self, 0, (60, 160))
        self.ports['negative'] = sb.Port(self, 1, (100, 160))

        # lines:
        self.lines.append(((80, 120), (80, 150)))
        self.lines.append(((60, 160), (100, 160)))

        # plus:
        self.lines.append(((60, 133), (60, 143)))
        self.lines.append(((55, 138), (65, 138)))

        # circle
        self.circles.append((75, 150, 10, 20))

        # rects:
        (w, h), m = self.size, self.margin
        self.rects.append(((0, 0, w, h, 5), (sb.DEVICE_COLOR, sb.SCOPE_BG)))
        window = m, m, w - m * 2, h - m * 2, 1
        self.rects.append((window, (sb.SCOPE_FG, sb.SCOPE_FG)))

    def end(self):
        times = self.engine.time
        values = self.engine.data

        n = len(times)

        npoints = 1000
        stride = int(n / npoints)
        stride = max(stride, 2)

        (w, h), m = self.size, self.margin

        if max(times) > 0.0:
            tscale = (w - m * 2.0) / max(times)
            toffset = m

            range_ = max(values) - min(values)

            mid = min(values) + range_ * 0.5

            iscale = 1.0
            if range_ > 0.0:
                iscale = -(h - m * 4.0) / range_

            self.margin = 12

            ioffset = -(mid * iscale - m * 5)

            # path:
            plot_curve = []
            for t, i in zip(times[::stride], values[::stride]):
                plot_curve.append((t * tscale + toffset, i * iscale + ioffset))

            self.plot_curves = []
            self.plot_curves.append((plot_curve, sb.SCOPE_CURVE))



    def get_engine(self, nodes):
        self.engine = IScope(nodes)
        return self.engine