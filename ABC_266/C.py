Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())

# 三角形の内部にtが存在するかチェック
# http://popopondelion.blog.fc2.com/blog-entry-6.html
def isInside(P1x, P1y, P2x, P2y, P3x, P3y, tx, ty):
    P1P2_X_P1t = 0
    P2P3_X_P2t = 0
    P3P1_X_P3t = 0

    P1P2_X_P1t = (P2x-P1x)*(ty-P1y) - (P2y-P1y)*(tx-P1x)
    P2P3_X_P2t = (P3x-P2x)*(ty-P2y) - (P3y-P2y)*(tx-P2x)
    P3P1_X_P3t = (P1x-P3x)*(ty-P3y) - (P1y-P3y)*(tx-P3x)

    if(( P1P2_X_P1t > 0.0 and P2P3_X_P2t > 0.0 and P3P1_X_P3t > 0.0) or ( P1P2_X_P1t < 0.0 and P2P3_X_P2t < 0.0 and P3P1_X_P3t < 0.0)):
        return 1
    else:
        return 0


for i in range(4):
    result_isInside = 0
    # Dを対象に調査（三角形ABC）
    if i == 0:
        result_isInside = isInside(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy)
    # Aを対象に調査（三角形BCD）
    elif i == 1:
        result_isInside = isInside(Bx, By, Cx, Cy, Dx, Dy, Ax, Ay)
    # Bを対象に調査（三角形CDA）
    elif i == 2:
        result_isInside = isInside(Cx, Cy, Dx, Dy, Ax, Ay, Bx, By)
    # Cを対象に調査（三角形DAB）
    else:
        result_isInside = isInside(Dx, Dy, Ax, Ay, Bx, By, Cx, Cy)

    if result_isInside == 1:
        print('No')
        exit()

print('Yes')